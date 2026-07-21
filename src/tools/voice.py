import platform


def voice_supported():

    return platform.system() == "Windows"
