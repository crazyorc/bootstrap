#!/usr/bin/python3

import devpipeline

class LayersCommand(devpipeline.common.GenericTool):

    """A bootstrap command that manages layer dependencies"""

    def __init__(self, tasks=None, executors=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument("layers", nargs="*",
                          help="The layers to operate on")
        self.tasks = tasks
        if executors:
            self.add_argument("--executor",
                              help="The amount of verbosity to use.  Options "
                                   "are \"quiet\" (print no extra "
                                   "information), \"verbose\" (print "
                                   "additional information), \"dry-run\" "
                                   "(print commands to execute, but don't run"
                                   " them), and \"silent\" (print nothing).  "
                                   "Regardless of this option, errors are "
                                   "always printed.",
                              default="quiet")
            self.add_argument("--cache-file",
                              help="Path to the build.cache file to use",
                              default=".cache/build.cache")
            self.verbosity = True
            self.executor = None
            self.components = None
            self.targets = None
        else:
            self.verbosity = False

    def execute(self, *args, **kwargs):
        parsed_args = self.parser.parse_args(*args, **kwargs)

        self.components = devpipeline.config.config.update_cache(cache_file=parsed_args.cache_file)
        if parsed_args.layers:
            self.layers = parsed_args.layers
        else:
            self.layers = self.components.sections()
        self.setup(parsed_args)
        if self.verbosity:
            helper_fn = devpipeline.EXECUTOR_TYPES.get(parsed_args.executor)
            if not helper_fn:
                raise Exception(
                    "{} isn't a valid executor".format(parsed_args.executor))
            else:
                self.executor = helper_fn()
        self.process()

    def process(self):
        layer_order = devpipeline.resolve.order_dependencies(
            self.layers, self.components)
        self.process_layers(layer_order)

    def process_layers(self, layer_order):
        """Executes the provided tasks against each layer"""
        config_info = {
            "executor": self.executor
        }
        for target in layer_order:
            self.executor.message("  {}".format(target))
            self.executor.message("-" * (4 + len(target)))
            current = self.components[target]
            env = devpipeline.common.create_target_environment(current)

            config_info["current_target"] = target
            config_info["current_config"] = current
            config_info["env"] = env
            for task in self.tasks:
                task(config_info)
            self.executor.message("")

