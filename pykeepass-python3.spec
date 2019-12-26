%global 	pypi_name pykeepass
%global         abi_package %{nil}

Name:           %{pypi_name}-python3
Version:        3.0.3
Release:        1%{?dist}
Summary:        Python library to interact with keepass databases (supports KDBX3 and KDBX4)

License:        GPLv3
URL:            https://github.com/pschmitt/pykeepass
Source:         https://github.com/pschmitt/pykeepass/archive/%{version}.tar.gz#/pykeepass-%{version}.tar.gz
BuildRequires:  python3-dev
Requires:       construct-python3
Requires:       python-future-python3
Requires:       lxml-python3
Requires:       pycryptodome-python3
Requires:       python-dateutil-python3

%description
pykeepass library allows you to write entries to a KeePass database.

%prep
%setup -n %{pypi_name}-%{version}
sed -i '1{/^#!.*env python/d}' pykeepass/pykeepass.py pykeepass/kdbx_parsing/kdbx*.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572997294
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build


%install
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 -tt setup.py build  install --root=%{buildroot}
rm -rvf %{buildroot}/usr/lib/python3*/tests


%files
%license LICENSE
%doc README.rst
/usr/lib/python3*/*


%changelog
# based on https://build.opensuse.org/package/show/openSUSE:Factory/python-pykeepass
