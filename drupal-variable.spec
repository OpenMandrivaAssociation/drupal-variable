%define modname		variable
%define drupal_version	7
%define module_version	2.1
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Variable module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}

%description
Variable module provides a registry for meta-data about Drupal variables
and some extended Variable API and administration interface.

This is an API module so it must be installed only when other modules require
it.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc README.txt


%changelog
* Thu Aug 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.2.1-1
+ Revision: 813184
- update to 7.x.2.1

* Sat May 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.1.2-1
+ Revision: 798432
- imported package drupal-variable

