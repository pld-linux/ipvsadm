Summary:	Utility to administer the Linux Virtual Server
Summary(pl):	Narzêdzie do administracji wirtualnymi serwerami
Name:		ipvsadm
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxvirtualserver.org/software/kernel-2.6/%{name}-%{version}.tar.gz
# Source0-md5:	a9378adf5af7a799535b4c26cf3bcf10
Source1:	%{name}-ip_vs.h
Patch0:		%{name}-make.patch
URL:		http://www.LinuxVirtualServer.org/
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

%description -l pl
ipvsadm jest narzêdziem do administracji wirtualnymi serwerami, co
umo¿liwia j±dro Linuksa z modu³ami IPVS (dostêpnymi jako ³ata od
d³u¿szego czasu, w³±czonymi do j±dra od 2.4.23). Ta wersja obs³uguje
wersje Linuksa 2.6.x.

%prep
%setup -q
%patch0 -p1

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
