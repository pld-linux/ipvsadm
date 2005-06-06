Summary:	Utility to administer the Linux Virtual Server
Summary(pl):	Narz�dzie do administracji wirtualnymi serwerami
Name:		ipvsadm
%define	ver	1.21
%define	rel	11
Version:	%{ver}.%{rel}
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxvirtualserver.org/software/kernel-2.4/%{name}-%{ver}-%{rel}.tar.gz
# Source0-md5:	6890a15e6b9887320b4582db2d89878d
Source1:	%{name}-ip_vs.h
Patch0:		%{name}-make.patch
URL:		http://www.LinuxVirtualServer.org/
BuildRequires:	popt-devel
Conflicts:	piranha <= 0.4.14
Conflicts:	kernel < 2.4.29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
ipvsadm is a utility to administer the IP virtual server services
offered by the Linux kernel augmented with the virtual server modules
(available as patch for long time, merged into kernel since 2.4.23).

%description -l pl
ipvsadm jest narz�dziem do administracji wirtualnymi serwerami, co
umo�liwia j�dro Linuksa z modu�ami IPVS (dost�pnymi jako �ata od
d�u�szego czasu, w��czonymi do j�dra od 2.4.23).

%prep
%setup -q -n %{name}-%{ver}-%{rel}
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
