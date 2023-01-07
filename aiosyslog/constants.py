from enum import Enum


class Proto(Enum):
    TCP = "tcp"
    UDP = "udp"
    UNIX = "unix"


class Severity(Enum):
    """Severity codes"""
    EMERG     = 0       #  system is unusable
    ALERT     = 1       #  action must be taken immediately
    CRIT      = 2       #  critical conditions
    ERR       = 3       #  error conditions
    WARNING   = 4       #  warning conditions
    NOTICE    = 5       #  normal but significant condition
    INFO      = 6       #  informational
    DEBUG     = 7       #  debug-level messages


class Facility(Enum):
    """Facility codes"""
    KERN      = 0       #  kernel messages
    USER      = 1       #  random user-level messages
    MAIL      = 2       #  mail system
    DAEMON    = 3       #  system daemons
    AUTH      = 4       #  security/authorization messages
    SYSLOG    = 5       #  messages generated internally by syslogd
    LPR       = 6       #  line printer subsystem
    NEWS      = 7       #  network news subsystem
    UUCP      = 8       #  UUCP subsystem
    CRON      = 9       #  clock daemon
    AUTHPRIV  = 10      #  security/authorization messages (private)
    FTP       = 11      #  FTP daemon
    NTP       = 12      #  NTP subsystem
    SECURITY  = 13      #  Log audit
    CONSOLE   = 14      #  Log alert
    SOLCRON   = 15      #  Scheduling daemon (Solaris)
    #  other codes through 15 reserved for system use
    LOCAL0    = 16      #  reserved for local use
    LOCAL1    = 17      #  reserved for local use
    LOCAL2    = 18      #  reserved for local use
    LOCAL3    = 19      #  reserved for local use
    LOCAL4    = 20      #  reserved for local use
    LOCAL5    = 21      #  reserved for local use
    LOCAL6    = 22      #  reserved for local use
    LOCAL7    = 23      #  reserved for local use

severety_names = {
    "alert":    Severity.ALERT,
    "crit":     Severity.CRIT,
    "critical": Severity.CRIT,
    "debug":    Severity.DEBUG,
    "emerg":    Severity.EMERG,
    "err":      Severity.ERR,
    "error":    Severity.ERR,        #  DEPRECATED
    "info":     Severity.INFO,
    "notice":   Severity.NOTICE,
    "panic":    Severity.EMERG,      #  DEPRECATED
    "warn":     Severity.WARNING,    #  DEPRECATED
    "warning":  Severity.WARNING,
}

#The map below appears to be trivially lowercasing the key. However,
#there's more to it than meets the eye - in some locales, lowercasing
#gives unexpected results. See SF #1524081: in the Turkish locale,
#"INFO".lower() != "info"
severety_map = {
    "DEBUG" : "debug",
    "INFO" : "info",
    "WARNING" : "warning",
    "ERROR" : "error",
    "CRITICAL" : "critical"
}

facility_names = {
    "auth":         Facility.AUTH,
    "authpriv":     Facility.AUTHPRIV,
    "console":      Facility.CONSOLE,
    "cron":         Facility.CRON,
    "daemon":       Facility.DAEMON,
    "ftp":          Facility.FTP,
    "kern":         Facility.KERN,
    "lpr":          Facility.LPR,
    "mail":         Facility.MAIL,
    "news":         Facility.NEWS,
    "ntp":          Facility.NTP,
    "security":     Facility.SECURITY,
    "solaris-cron": Facility.SOLCRON,
    "syslog":       Facility.SYSLOG,
    "user":         Facility.USER,
    "uucp":         Facility.UUCP,
    "local0":       Facility.LOCAL0,
    "local1":       Facility.LOCAL1,
    "local2":       Facility.LOCAL2,
    "local3":       Facility.LOCAL3,
    "local4":       Facility.LOCAL4,
    "local5":       Facility.LOCAL5,
    "local6":       Facility.LOCAL6,
    "local7":       Facility.LOCAL7,
}

class FramingMethod(Enum):
    OCTET_COUNTING = 0
    NON_TRANSPARENT_FRAMING = 1

class FrameTrailer(Enum):
    LF = "\n"
    CRLF = "\r\n"
    NULL = "\0"