#!/usr/bin/env python
import sys
import os
import subprocess
import glob
import shutil
from setuptools import setup, find_packages
import distutils

class CiBuild(object):

    def __init__(self):
        self._root_model = 'openhltest.yang'
        self._root_dir = os.getcwd()
        self._python = os.path.normpath(sys.executable)
        self._python_dir = os.path.dirname(self._python)
        self._view_models_dir = os.path.normpath('%s/views' % self._root_dir)
        self._openhltest_dir = os.path.normpath('%s/python_client/openhltest' % self._root_dir)
        if os.name == 'nt':
            self._pyang = os.path.normpath('%s/scripts/pyang' % self._python_dir)
        else:
            self._pyang = self._find('pyang', os.path.normpath('%s/..' % self._python_dir))
        # if 'TRAVIS_BRANCH' in os.environ.keys():
            # self._branch = os.environ['TRAVIS_BRANCH']
        # else:
            # self._branch = 'master'
        # self._commit_range = None
        # if 'TRAVIS_COMMIT_RANGE' in os.environ.keys():
            # self._commit_range = os.environ['TRAVIS_COMMIT_RANGE']
        print('pyang location %s' % self._pyang)
        self._data_models_dir = os.path.normpath('%s/models' % self._root_dir)
        print('data models location %s' % self._data_models_dir)
        self._python_client_dir = os.path.join(self._root_dir, 'python_client')
        # with open(os.path.join(self._python_client_dir, 'CURRENT_BUILD_NUMBER.txt')) as fid:
            # self._build_number = fid.read()
            # self._version = '0.1a%s' % (self._build_number)
        # process_args = [
            # 'git',
            # 'checkout',
            # self._branch
        # ]
        # self._run_process(process_args, self._root_dir)
        # process_args = [
            # 'git',
            # 'remote'
        # ]
        # self._run_process(process_args, self._root_dir)
        # process_args = [
            # 'git',
            # 'config',
            # '--list'
        # ]
        # self._run_process(process_args, self._root_dir)		

    def _find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def _run_process(self, process_args, default_dir, redirect_stdout_to=None):
        self._process_output = ''
        fid = None
        if redirect_stdout_to is not None:
            fid = open(os.path.join(default_dir, redirect_stdout_to), 'w')
        process = subprocess.Popen(process_args, bufsize=1, cwd=default_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while process.returncode is None:
            stdout_data, stderr_data = process.communicate()
            stdout_data = stdout_data.decode('utf-8')
            stderr_data = stderr_data.decode('utf-8')
            if process.returncode == 0:
                if fid is not None:
                    fid.write(stdout_data)
                    fid.close()
                else:
                    print(stdout_data)
                    self._process_output += stdout_data
                return 0
            elif process.returncode > 0:
                print('PROCESS FAIL: %s' % stderr_data)
                return process.returncode
            else:
                if fid is not None:
                    fid.write(stdout_data)
                else:
                    print(stdout_data)
                    self._process_output += stdout_data

    def _git_add(self, filename):
        pass;
        # print('git add of %s' % filename)
        # process_args = [
            # 'git',
            # 'add',
            # '--all',
            # filename
        # ]
        # self._run_process(process_args, self._root_dir)

    def _git_commit_push(self):
        pass;
        # process_args = [
            # 'git',
            # 'commit',
            # '-m "upload auto generated model views, python client documentation [skip ci]"'
        # ]
        # self._run_process(process_args, self._root_dir)
        # process_args = [
            # 'git',
            # 'push',
            # 'https://%s@github.com/OpenHLTest/data-models.git' %(os.environ['GH_TOKEN']),
            # self._branch
        # ]
        # self._run_process(process_args, self._root_dir)

    def check_changed_files(self):
        pass;
        # print('checking for changed files...')
        # process_args = [
            # 'git',
            # 'diff',
            # '--name-only'
        # ]
        # if self._commit_range is not None:
            # process_args.append(self._commit_range)
        # if self._run_process(process_args, self._root_dir) == 0:
            # continue_build = False
            # for changed_file in self._process_output.split('\n'):
                # if changed_file.startswith('model/') or changed_file.startswith('python_client/') or changed_file.startswith('plugins/'):
                    # continue_build = True
            # if continue_build is False:
                # print('stopping build, no model or client generation updates')
                # sys.exit(0)
        # else:
            # print('stopping build, git diff failed')
            # sys.exit(1)

    def validate_models(self):
        print('validating openhltest models...')
        validate = [
            self._python,
            self._pyang,
            '--strict',
            '--path',
            self._data_models_dir,
            self._root_model
        ]
        if self._run_process(validate, self._data_models_dir) > 0:
            print('model validation failed')
            sys.exit(1)

    def generate_model_views(self):
        for view_format, view_ext in [('tree', 'txt'), ('jstree', 'html')]:
            output_file = os.path.normpath('%s/openhltest_model.%s' %(self._view_models_dir, view_ext))
            if os.path.exists(output_file):
                os.unlink(output_file)
            print('generating %s model view...' % view_format)
            view = [
                self._python,
                self._pyang,
                '--strict',
                '--format',
                view_format,
                '--output',
                output_file,
                '--path',
                self._data_models_dir,
                self._root_model
            ]
            if self._run_process(view, self._data_models_dir) > 0:
                print('generate model views failed')
                sys.exit(1)
            self._git_add(output_file)

    def generate_openhltest_client(self):
        setup_dir = os.path.normpath('%s/python_client' % self._root_dir)
        plugins_dir = os.path.normpath('%s/plugins' % self._root_dir)
        output_file = os.path.normpath('%s/openhltest/openhltest.py' % (setup_dir))
        if os.path.exists(output_file):
            os.unlink(output_file)
        print('auto generating openhltest python client from yang models...')
        client = [
            self._python,
            self._pyang,
            '--strict',
            '--format',
            'openhltest',
            '--output',
            output_file,
            '--path',
            self._data_models_dir,
            '--plugindir',
            plugins_dir,
            self._root_model
        ]
        if self._run_process(client, self._data_models_dir) > 0:
            print('auto generation of python client from models failed')
            sys.exit(1)
        self._git_add(output_file)


    def generate_python_documentation(self):
        print('generating client documentation...')
        # output_file = 'openhltest.md'
        # docs_dir = os.path.normpath('%s/python_client/openhltest/docs' % self._root_dir)
        # process_args = [
            # self._python,
            # os.path.normpath('%s/pydocmd.py' % self._root_dir),
            # 'simple',
            # 'openhltest'
        # ]
        # self._run_process(process_args, docs_dir, redirect_stdout_to=output_file)
        # self._git_add(os.path.join(docs_dir, output_file))

        if os.name == 'nt':
            process_args = [
                self._python,
                os.path.normpath('%s/Lib/pydoc.py' % self._python_dir),
                '-w',
                'openhltest'
            ]
        else:
            process_args = [
                'pydoc',
                '-w',
                'openhltest'
            ]
        output_file = 'openhltest.html'
        docs_dir = os.path.normpath('%s/python_client/openhltest' % self._root_dir)
        self._run_process(process_args, docs_dir)
        self._git_add(os.path.join(docs_dir, output_file))

    def move_model_views_to_openhltest_client(self):
        print('including model documentation in python client documentation...')
        for filename in os.listdir(self._view_models_dir):
            src = os.path.join(self._view_models_dir, filename)
            dst = os.path.join(self._openhltest_dir, 'docs', filename)
            shutil.copyfile(src, dst)
            self._git_add(dst)

    def update_repository(self):
        print('commit and push of updated files')
        self._git_commit_push()



cibuild = CiBuild()
cibuild.validate_models()
cibuild.generate_model_views()
cibuild.generate_openhltest_client()
cibuild.generate_python_documentation()
