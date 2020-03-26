import logging

from notion.client import NotionClient
from notion.collection import NotionDate


class NotionTasksClient:
    def __init__(self, conf):
        self.conf = conf
        if 'token_v2' not in self.conf or 'block_url' not in self.conf:
            raise KeyError("Specify the properties token_v2 and block_url in \
                the config notion section")

        self.client = NotionClient(token_v2=conf['token_v2'])
        self.page = self.client.get_block(conf['block_url'])
        logging.info("Using Notion page " + self.page.title)

    def create_task(self, task):
        title = task['title']
        due_date = task['due_date'] if 'due_date' in task else None
        logging.info("Creating task in notion. Summary: %s - Due date: %s",
                     title, due_date)
        self.page.collection.get_rows()
        newrow = self.page.collection.add_row()
        newrow.title = title
        if due_date:
            start_date = due_date.strftime("%Y-%m-%d")
            notionDate = NotionDate.from_notion({"start_date": start_date})
            newrow.due_date = notionDate
        return newrow
