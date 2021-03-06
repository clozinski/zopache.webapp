from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as file:
        return file.read()

setup(name='zopache.webapp',
      version='0.1',
      description='Zopache Web Application',
      long_description=(
        read('README.txt')
        ),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      keywords='zope bluebream ttw',
      author='Christopher Lozinski',
      author_email='lozinski@freerecruiting.com',
      url='http://zopache.com',
      license='ZPL 2.1',
      package_dir={'': 'src'},
      packages=find_packages('src'),

      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'z3c.pt',
        'z3c.template',
        'z3c.testsetup',
        'zopache.pagetemplate',
	'zopache.pythonscript',
        'zope.app.apidoc',
        'zope.app.appsetup',
        'zope.app.basicskin',
        'zope.app.broken',
        'zope.app.catalog',
        'zope.app.content',
        'zope.app.component',
        'zope.app.container',
        'zope.app.debug',
        'zope.app.dependable',
        'zope.app.error',
        'zope.app.file',
        'zope.app.folder',
        'zope.app.form',
        'zope.app.generations',
        'zope.app.i18n',
        'zope.app.intid',
        'zope.app.locales',
        'zope.app.pagetemplate',
        'zope.app.principalannotation',
        'zope.app.publisher',
        'zope.app.rotterdam',
        'zope.app.schema',
        'zope.app.security',
        'zope.app.session',
        'zope.app.testing',
        'zope.app.wsgi',
        'zope.app.zcmlfiles',
        'zope.app.zopeappgenerations',
        'zope.annotation',
        'zope.browserresource',
        'zope.catalog',
        'zope.component',
        'zope.contentprovider',
        'zope.fanstatic',
        'zope.formlib',
        'zope.i18n',
        'zope.intid',
        'zope.keyreference',
        'zope.login',
        'zope.publisher',
        'zope.securitypolicy',
        'zope.sendmail',
        'zope.testbrowser',
        'ztfy.blog',
        'ztfy.scheduler',
        'ztfy.zmi',
        ],
      entry_points = """
      [paste.app_factory]
      main = zopache.webapp.startup:application_factory

      [paste.global_paster_command]
      shell = zopache.webapp.debug:Shell
      """,
      )
