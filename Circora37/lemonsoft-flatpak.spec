Name:           lemonsoft-repo
Version:        0.0.1
Release:        1%{?dist}
Summary:        Lemonade Repository
BuildArch:      noarch

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

%description
Lemonade repository for Lemonade OS

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
cp etc/yum.repos.d/lemonsoftplus.repo $RPM_BUILD_ROOT/etc/yum.repos.d
#cp %{name}.spec $RPM_BUILD_ROOT/etc/yum.repo.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
/etc/yum.repos.d/lemonsoftplus.repo

%changelog
* Mon May  30 2022 MiMillie - 0.0.1
- First version being packaged
