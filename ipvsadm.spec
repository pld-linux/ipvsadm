Summary:	Utility to administer the Linux Virtual Server
Summary(pl):	Narzêdzie do administracji wirtualnymi serwerami
Name:		ipvsadm
Version:	1.15
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.linuxvirtualserver.org/software/%{name}-%{version}.tar.gz
URL:		http://www.LinuxVirtualServer.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	piranha <= 0.4.14

%define		_sbindir	/sbin

%description
ipvsadm is a utility to administer the IP virtual server services
offered by the Linux kernel augmented with the virtual server patch.

%description -l pl
ipvsadm jest narzêdziem do administracji wirtualnymi serwerami,
mo¿liwo¶æ taka dostêpna po spatchowaniu kernela patchem linux-ipvs

%prep
%setup -q -n ipvsadm

%build
CFLAGS="%{rpmcflags}" make


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install BUILD_ROOT=${RPM_BUILD_ROOT}

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README

%clean
rm -rf $RPM_BUILD_DIR

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/ipvsadm
%{_mandir}/man8/ipvsadm.8*
