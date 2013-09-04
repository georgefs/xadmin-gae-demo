import site
import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
SITE_PATH = os.path.join(CUR_PATH, 'site-packages/')

site.addsitedir(SITE_PATH)

SITE_PATH = os.path.join(CUR_PATH, 'demo_app/')
site.addsitedir(SITE_PATH)


#os.environ['GOOGLE_SQL_OAUTH2_REFRESH_TOKEN'] = "1/oBl4zHM5miWHllLsKkGzXp7mFVvkFo9ZBae9gKAZBaw"
