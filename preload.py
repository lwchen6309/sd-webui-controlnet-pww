def preload(parser):
    is_controlnet_loaded = any(arg.dest == 'controlnet_dir' for arg in parser._actions) or any(arg.dest == 'no_half_controlnet' for arg in parser._actions)
    if not is_controlnet_loaded:
        parser.add_argument("--controlnet-dir", type=str, help="Path to directory with ControlNet models", default=None)
        parser.add_argument("--no-half-controlnet", action='store_true', help="do not switch the ControlNet models to 16-bit floats (only needed without --no-half)", default=None)