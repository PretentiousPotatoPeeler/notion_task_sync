import logging
import caldav


class CalDAVTasksClient:

    def __init__(self, conf):
        self.conf = conf
        if ('username' not in self.conf or 'password' not in self.conf
                or 'url' not in self.conf):
            raise KeyError("Specify the properties username, password, url and \
                inbox_name in the config notion section")
        self.url = "https://" + conf['username'] + ":" + conf['password'] + \
            "@" + conf['url'] + "/remote.php/caldav/calendars/" + \
            conf['username'] + "/"
        logging.info("Using url %s", self.url)

        client = caldav.DAVClient(self.url)
        principal = client.principal()
        calendars = principal.calendars()

        def cal_filter(c):
            return str(c).endswith(conf['inbox_name'] + '/')

        filtered_calendars = list(filter(cal_filter, calendars))
        if len(filtered_calendars) > 0:
            self.inbox_calendar = filtered_calendars[0]
            logging.info("Using calendar %s", str(self.inbox_calendar))
        else:
            raise KeyError("Could not find inbox calendar")

    def get_tasks(self):
        return [self._format_task(t) for t in self.inbox_calendar.todos()]

    def delete_task(self, task):
        logging.info("Deleting task %s", task['title'])
        task['original_object'].delete()

    def _format_task(self, task):
        result = {
            "title": task.instance.vtodo.summary.value,
            "original_object": task
        }
        if hasattr(task.instance.vtodo, 'due'):
            result['due_date'] = task.instance.vtodo.due.value
        return result
