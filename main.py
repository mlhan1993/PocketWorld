from src.app import APP, APPConfig
from src.db import DB, DBConfig

def main():
    db_config = DBConfig({
        'table_name': 'URLShortener'
    })
    db = DB(db_config)

    appConfig = APPConfig(1)
    app = APP(appConfig, db)
    app.run()


if __name__ == '__main__':
    main()
