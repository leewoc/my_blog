"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8)qc_82gq)mxqsrr$4irf4(kd)*9ns96u#xxvws57v^od(yvg="

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ckeditor",  # 富文本编辑器
    "ckeditor_uploader",  # 富文本编辑器上传图片模块
    "blog",
    "read_count",
    "comment",
    "likes",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "djangoProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "user.context_processors.login_modal_form",
            ],
        },
    },
]

WSGI_APPLICATION = "djangoProject.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mysite",
        "USER": "root",
        "PASSWORD": "12138",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'zh-hans'  # 语言：简体中文
#
# TIME_ZONE = 'Asia/Shanghai'  # 亚洲上海
#
# USE_I18N = True
#
# USE_TZ = True
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = "upload/"

# 使用ck的工具栏并修改，宽度自适应
CKEDITOR_CONFIGS = {
    # django-ckeditor默认使用default配置
    'default': {
        # 编辑器宽度自适应
        'width': 'auto',
        'height': '100px',
        # tab键转换空格数
        'tabSpaces': 4,
        # 工具栏风格
        'toolbar': 'Custom',
        # 工具栏按钮
        'toolbar_Custom': [
            # 预览、表情
            ['Preview', 'Smiley'],
            # 字体风格
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
            # 字体颜色
            ['TextColor', 'BGColor'],
            # 格式、字体、大小
            ['Format', 'Font', 'FontSize'],
            # 链接
            ['Link', 'Unlink'],
            # 列表
            ['Image', 'NumberedList', 'BulletedList'],
            # 居左，居中，居右
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            # 最大化
            ['Maximize']
        ],
        # 去除HTML标签提示
        'removePlugins': 'elementspath',
        'resize_enabled': 'False',
        # 加入代码块插件
        'extraPlugins': ','.join(['codesnippet', 'image2', 'filebrowser', 'widget', 'lineutils']),
    },
    # 评论
    # 'comment': {
    #     # 编辑器宽度自适应
    #     'width': 'auto',
    #     'height': '140px',
    #     # tab键转换空格数
    #     'tabSpaces': 4,
    #     # 工具栏风格
    #     'toolbar': 'Custom',
    #     # 工具栏按钮
    #     'toolbar_Custom': [
    #         # 表情 代码块
    #         ['Smiley', 'CodeSnippet'],
    #         # 字体风格
    #         ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
    #         # 字体颜色
    #         ['TextColor', 'BGColor'],
    #         # 链接
    #         ['Link', 'Unlink'],
    #         # 列表
    #         ['NumberedList', 'BulletedList'],
    #     ],
    #     # 加入代码块插件
    #     'extraPlugins': ','.join(['codesnippet']),
    # }
}
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False

# 缓存设置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
# 发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465  # 端口号
EMAIL_HOST_USER = '########'  # 邮箱地址
EMAIL_HOST_PASSWORD = '###########'  # 授权码
EMAIL_SUBJECT_PREFIX = '[Leewoc的博客]'
EMAIL_USE_SSL = True
