%global _empty_manifest_terminate_build 0
Name:       python-aiosmtpd
Version:    1.2.2
Release:    1
Summary:    aiosmtpd - asyncio based SMTP server
License:    Apache 2.0
URL:        https://github.com/aio-libs/aiosmtpd
Source0:    https://github.com/aio-libs/aiosmtpd/archive/%{version}.tar.gz
BuildArch:  noarch

%description
This is a server for SMTP and related protocols, similar in utility to the
standard library's smtpd.py module, but rewritten to be based on asyncio for
Python 3.

%package -n python3-aiosmtpd
Summary:        aiosmtpd - asyncio based SMTP server
Provides:       python-aiosmtpd
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-aiosmtpd
This is a server for SMTP and related protocols, similar in utility to the
standard library's smtpd.py module, but rewritten to be based on asyncio for
Python 3.

%package help
Summary:    Development documents and examples for aiosmtpd
Provides:   python3-aiosmtpd-doc

%description help
Development documents and examples for aiosmtpd.

%prep
%autosetup -n aiosmtpd-%{version}

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-aiosmtpd -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_pkgdocdir}

%changelog
* Thu Dec 17 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
