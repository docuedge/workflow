"""
Django settings for Workflow_Django project.

Generated by 'django-admin startproject' using Django 2.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l(xo)96__pp!zd%yq1lf91vk2_gj4$0!3p91)iyyl1$=w_xc$f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Third party app
    'rest_framework',
    #Project's app
    'workflow_vault',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'workflow_vault.authentication.CognitoAuthentication',  
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Workflow_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Workflow_Django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

USER_GROUPS = ["demogroup1", "dms-admin"]
ALL_GROUPS = []

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Project constant

CONSTANT_URL = 'https://8mjigfuo2i.execute-api.us-east-2.amazonaws.com/dev/rest/server/'

# PROCESS_NAME=["Review", "Approval"]


# REVIEW_CONTAINER_ID="business-application-kjar-1_0-SNAPSHOT"
# APPROVAL_CONTAINER_ID="business-application-kjar-1_0-SNAPSHOT"

# REVIEW_PROCESS_ID = "business-application-kjar.Doc_Review"
# APPROVAL_PROCESS_ID="business-application-kjar.vault-doc-approval"


COGNITO_USER_POOL_ID = 'us-east-2_UyaMlyxfj'
COGNITO_CLIENT_ID = '2kntuk8e2f9jg75pdi92rrbttu'
COGNITO_CLIENT_SECRET = 'kr1kh5p1mlesb1r30986sjekmsvl4rvi5fguajbgd2t5gqg9opr'
AWS_REGION = 'us-east-2'

#AWS Deloitte
ACCESS_KEY = 'AKIASCJAS4TMPQER4RG6'
ACCESS_SECRET = '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'
    
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
