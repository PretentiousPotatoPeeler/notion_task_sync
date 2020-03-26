# Notion Task Sync

Sync tasks from a todo platform to a Notion database

## Motivation

The Notion app is too slow. Sometimes I want to jot something down real quick, and the Notion android app just doesn't cut it. Todo-list apps are way better, and are sort of made for this. This python script for now moves Todo's from a CalDAV calendar to a Notion database. 

*NOTE: The original todo is deleted when it's added to the Notion database.*
This works for me as I want Notion to be my leading source of truth. Future implementations will actually sync the two.

## Usage

```bash
pip install -r requirements.txt
python notion_task_sync.py ./notion_task_sync.conf
```

Config file example is in the repo.

### Docker

To build and run docker image use:
```bash
docker build -t notion_task_sync .
docker run --name notion_task_sync notion_task_sync
```

## Built With

* [notion-py](https://github.com/jamalex/notion-py) - The Notion lib used
* [caldav](https://github.com/python-caldav/caldav) - The CalDAV lib used

## Contributing

Feel free to submit an issue or pull request. It'd even be really cool if you did :)

## License

This project is licensed under the DBAD License - see the [LICENSE.md](LICENSE.md) file for details
