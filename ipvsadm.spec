Summary:	Utility to administer the Linux Virtual Server
Summary(pl.UTF-8):	Narzędzie do administracji wirtualnymi serwerami
Name:		ipvsadm
Version:	1.25
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxvirtualserver.org/software/kernel-2.6/%{name}-%{version}.tar.gz
# Source0-md5:	772a053f5fe888cd25784c5f55d31fc3
Source1:	%{name}-ip_vs.h
Patch0:		%{name}-make.patch
Patch1:		%{name}-activeconn.patch
URL:		http://www.LinuxVirtualServer.org/
BuildRequires:	libnl-devel
BuildRequires:	popt-devel
Conflicts:	ipvsadm24
Conflicts:	piranha <= 0.4.14
#Conflicts:	kernel < 2.6.?
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
ipvsadm is a utility to administer the IP virtual server services
offered by the Linux kernel augmented with the virtual server modules
(available as patch for long time, merged into kernel since 2.4.23).
This version supports Linux 2.6.x series.

%description -l pl.UTF-8
ipvsadm jest narzędziem do administracji wirtualnymi serwerami, co
umożliwia jądro Linuksa z modułami IPVS (dostępnymi jako łata od
dłuższego czasu, włączonymi do jądra od 2.4.23). Ta wersja obsługuje
wersje Linuksa 2.6.x.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

cp -f %{SOURCE1} ip_vs.h

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILD_ROOT=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/ipvsadm
%attr(755,root,root) %{_sbindir}/ipvsadm-save
%attr(755,root,root) %{_sbindir}/ipvsadm-restore
%{_mandir}/man8/ipvsadm.8*
%{_mandir}/man8/ipvsadm-save.8*
%{_mandir}/man8/ipvsadm-restore.8*
