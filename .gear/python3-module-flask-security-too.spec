%define pypi_name flask-security-too

%def_without check

Name:    python3-module-%pypi_name
Version: 5.3.0
Release: alt1

Summary: Quick and simple security for Flask applications
License: MIT
Group:   Development/Python3
URL:     https://github.com/Flask-Middleware/flask-security

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-flask
BuildRequires: python3-module-pytest
%endif
BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst AUTHORS LICENSE
%python3_sitelibdir/flask_security/
%python3_sitelibdir/Flask_Security_Too-%version.dist-info/

%changelog
* Wed Oct 04 2023 Danilkin Danila <danild@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus
