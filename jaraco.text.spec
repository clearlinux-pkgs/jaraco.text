#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jaraco.text
Version  : 3.2.0
Release  : 12
URL      : https://files.pythonhosted.org/packages/03/3e/4fd93c4ca0524b3a55ab6c9a1cc5e2ec4fdbf6cfbf4c23a2fbfcf450e348/jaraco.text-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/03/3e/4fd93c4ca0524b3a55ab6c9a1cc5e2ec4fdbf6cfbf4c23a2fbfcf450e348/jaraco.text-3.2.0.tar.gz
Summary  : Module for text manipulation
Group    : Development/Tools
License  : MIT
Requires: jaraco.text-license = %{version}-%{release}
Requires: jaraco.text-python = %{version}-%{release}
Requires: jaraco.text-python3 = %{version}-%{release}
Requires: jaraco.functools
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : jaraco.functools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jaraco.text.svg
:target: https://pypi.org/project/jaraco.text

%package license
Summary: license components for the jaraco.text package.
Group: Default

%description license
license components for the jaraco.text package.


%package python
Summary: python components for the jaraco.text package.
Group: Default
Requires: jaraco.text-python3 = %{version}-%{release}

%description python
python components for the jaraco.text package.


%package python3
Summary: python3 components for the jaraco.text package.
Group: Default
Requires: python3-core
Provides: pypi(jaraco.text)
Requires: pypi(jaraco.functools)
Requires: pypi(six)

%description python3
python3 components for the jaraco.text package.


%prep
%setup -q -n jaraco.text-3.2.0
cd %{_builddir}/jaraco.text-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583536075
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jaraco.text
cp %{_builddir}/jaraco.text-3.2.0/LICENSE %{buildroot}/usr/share/package-licenses/jaraco.text/a1474494d96f6ddb3a9a0d767a09871ffc388faf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.*/site-packages/jaraco/__init__.py
rm -f %{buildroot}/usr/lib/python3.*/site-packages/jaraco/__pycache__/__init__.*

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jaraco.text/a1474494d96f6ddb3a9a0d767a09871ffc388faf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
