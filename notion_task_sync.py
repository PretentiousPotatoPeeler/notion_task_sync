import logging
import configparser
import argparse

from integrations.notion_tasks_client import NotionTasksClient
from integrations.caldav_tasks_client import CalDAVTasksClient

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('config_file_location', type=str,
                    help='path to config file location')


def move_tasks(notion_client, tasks_client):
    for task in tasks_client.get_tasks():
        notion_task = notion_client.create_task(task)
        try:
            tasks_client.delete_task(task)
        except Exception:
            logging.exception("Could not delete origin task, \
                deleting notion task as well")
            notion_task.remove()


def load_config(file_location):
    config = configparser.ConfigParser()
    config.read(file_location)
    return config


def main(args):
    conf = load_config(args.config_file_location)
    notion_client = NotionTasksClient(conf['notion'])

    if 'caldav' in conf:
        logging.info("Syncing using CalDAV")
        caldav_client = CalDAVTasksClient(conf['caldav'])
        move_tasks(notion_client, caldav_client)


if __name__ == "__main__":
    main(parser.parse_args())
