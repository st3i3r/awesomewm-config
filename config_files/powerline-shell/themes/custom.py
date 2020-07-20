
from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 196
    USERNAME_BG = 232
    USERNAME_ROOT_BG = 0

    HOSTNAME_FG = 82
    HOSTNAME_BG = 232

    HOME_SPECIAL_DISPLAY = True
    PATH_BG = 232  # dark grey
    PATH_FG = 222  # light grey
    CWD_FG = 214
    SEPARATOR_FG = 4

    READONLY_BG = 232
    READONLY_FG = 15

    REPO_CLEAN_BG = 232   # green
    REPO_CLEAN_FG = 154  # black
    REPO_DIRTY_BG = 232   # red
    REPO_DIRTY_FG = 154 # white

    JOBS_FG = 14
    JOBS_BG = 232

    CMD_PASSED_BG = 232
    CMD_PASSED_FG = 82
    CMD_FAILED_BG = 232
    CMD_FAILED_FG = 196

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 232
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 232
    AWS_PROFILE_BG = 8

    TIME_FG = 190
    TIME_BG = 232

    BAT_BG = 232
