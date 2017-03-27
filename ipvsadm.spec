# TODO: PLDify init script
Summary:	Utility to administer the Linux Virtual Server
Summary(pl.UTF-8):	Narzędzie do administracji wirtualnymi serwerami
Name:		ipvsadm
Version:	1.29
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/kernel/ipvsadm/%{name}-%{version}.tar.xz
# Source0-md5:	12f0d3b4d436e941d0c4dbe358144bfd
Patch0:		%{name}-make.patch
URL:		http://www.LinuxVirtualServer.org/
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	popt-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Conflicts:	ipvsadm24
Conflicts:	piranha <= 0.4.14
Requires:	uname(release) >= 2.6
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

%build
%{__make} -j1 \
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
%doc MAINTAINERS README
%attr(755,root,root) %{_sbindir}/ipvsadm
%attr(755,root,root) %{_sbindir}/ipvsadm-save
%attr(755,root,root) %{_sbindir}/ipvsadm-restore
#%attr(754,root,root) /etc/rc.d/init.d/ipvsadm
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ipvsadm
%{_mandir}/man8/ipvsadm.8*
%{_mandir}/man8/ipvsadm-save.8*
%{_mandir}/man8/ipvsadm-restore.8*
