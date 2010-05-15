%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		BuildNotify
Version:	0.2.5
Release:	1%{?dist}
Summary:	Cruise Control build monitor for Windows/Linux/Mac
Group:		Applications/Productivity
License:	GPLv3
URL:		http://bitbucket.org/Anay/buildnotify/
Source0:	http://pypi.python.org/packages/source/B/BuildNotify/BuildNotify-0.2.5.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	python2-devel, pytz, python-setuptools, python-dateutil, PyQt4

%description
BuildNotify is a cruise control system tray monitor which works on Windows/Linux/Mac. 
It was largely inspired from CCMenu and lets you monitor multiple continuous integration 
servers with customizable build notifications for all projects.

%prep
%setup -q

find %{buildroot}/%{python_sitelib} -name '*.pyc' | xargs rm -f
find %{buildroot}/%{python_sitelib} -name '*.egg-info' | xargs rm -f

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

find %{buildroot}/%{python_sitelib} -name '*.exe' | xargs rm -f

%check
%{__python} setup.py test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/buildnotifylib/*
%{python_sitelib}/BuildNotify*egg-info
%{_bindir}/buildnotifyapplet.py

%changelog
* Tue Mar 30 2010 Anay Nayak <anayak007 at, gmail.com> 2.5-1
- Added tag v0.2.5 for changeset 47d56dab5ea3