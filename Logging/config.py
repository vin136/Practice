import mylogger
import logging

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
      "simple": {
        "format": "%(levelname)s: %(message)s",
        "datefmt": "%Y-%m-%dT%H:%M:%S%z"
      },
      "json": {
        "()": "mylogger.MyJSONFormatter",
        "fmt_keys": {
          "level": "levelname",
          "message": "message",
          "timestamp": "timestamp",
          "logger": "name",
          "module": "module",
          "function": "funcName",
          "line": "lineno",
          "thread_name": "threadName"
        }
      }
    },
    "handlers": {
      "stderr": {
        "class": "logging.StreamHandler",
        "level": "WARNING",
        "formatter": "simple",
        "stream": "ext://sys.stderr"
      },
      "file": {
        "class": "logging.handlers.RotatingFileHandler",
        "level": "DEBUG",
        "formatter": "json",
        "filename": "logs/my_app.log.jsonl",
        "maxBytes": 10000,
        "backupCount": 3
      }
    },
    "loggers": {
      "root": {
        "level": "DEBUG",
        "handlers": [
          "stderr",
          "file"
        ]
      }
    }
  }



logging_config_queue = {
  "version": 1,
  "disable_existing_loggers": False,
  "formatters": {
    "simple": {
      "format": "[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s",
      "datefmt": "%Y-%m-%dT%H:%M:%S%z"
    },
    "json": {
      "()": "mylogger.MyJSONFormatter",
      "fmt_keys": {
        "level": "levelname",
        "message": "message",
        "timestamp": "timestamp",
        "logger": "name",
        "module": "module",
        "function": "funcName",
        "line": "lineno",
        "thread_name": "threadName"
      }
    }
  },
  "handlers": {
    "stderr": {
      "class": "logging.StreamHandler",
      "level": "WARNING",
      "formatter": "simple",
      "stream": "ext://sys.stderr"
    },
    "file_json": {
      "class": "logging.handlers.RotatingFileHandler",
      "level": "DEBUG",
      "formatter": "json",
      "filename": "logs/my_app.log.jsonl",
      "maxBytes": 10000,
      "backupCount": 3
    },
    "queue_handler": {
      "class": "logging.handlers.QueueHandler",
      "handlers": [
        "stderr",
        "file_json"
      ],
      "respect_handler_level": True
    }
  },
  "loggers": {
    "root": {
      "level": "DEBUG",
      "handlers": [
        "queue_handler"
      ]
    }
  }
}
# Logger
logging.config.dictConfig(logging_config)
logger = logging.getLogger()