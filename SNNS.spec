
%define ftppath ftp://ftp.informatik.uni-stuttgart.de/pub/SNNS

Summary:	Stuttgart Neural Network Simulator
Summary(de):	Stuttgart Neural Network Simulator
Summary(pl):	Stuttgart Neural Network Simulator
Name:		SNNS
Version:	4.1
Release:	0.1
License:	Free Software
Group:		X11/Applications
Source0:	%{ftppath}/%{name}v%{version}.tar.gz
# Source0-md5:	6385faf45eec7bfba67d7024c31d1ac0
Source2:	%{ftppath}/%{name}v%{version}.Manual.ps.gz
# Source2-md5:	09431050aa7c3c77f55751566149c853
Source3:	%{ftppath}/%{name}info-1.03.tar.gz
# Source3-md5:	c2a99f0294bd02e5f3bfdff6bf16469a
Patch1:		%{name}-config.diff
Patch2:		%{name}-XGUILOADPATH.diff
Patch3:		%{name}-inc_fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
%{name} (Stuttgart Neural Network Simulator) is a nuron network simulator

%description -l de
%{name} (Stuttgart Neural Network Simulator) ist ein Simulationsprogramm
für Neuronal Netzwerk.

%description -l pl
%{name} (Stuttgar Neural Network Simulator) jest symulatorem sieci nuronwych.

%package doc
Summary:	SNNS-Dokomentationen
Group:		X11/Applications

%desc 
Documentation for %{name} in html and postscript.

%description -l de doc
Dieses Paket enthält die Dokumentationen in html und
Postscript-Format.

%description -l pl
Ten pakiet zawiera dokumentacje w htmlu i postscripcie.

%prep
%setup -q -n %{name}v%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} -C kernel/sources
%{__make} -C tools/sources
%{__make} -C xgui/sources

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/SNNS/{kernel,tools,xgui}/bin/pc_linux \
$RPM_BUILD_ROOT%{_prefix}/{bin,lib/SNNS/examples}

%{__make} -C kernel/sources install \
		DESTDIR=$RPM_BUILD_ROOT 
		
%{__make} -C xgui/sources install \
		DESTDIR=$RPM_BUILD_ROOT

%{__make} -C tools/sources install \
		DESTDIR=$RPM_BUILD_ROOT

cp -af help.hdoc default.cfg examples $RPM_BUILD_ROOT%{_libdir}/SNNS

ln -fs ../../lib/SNNS/xgui/bin/pc_linux/xgui \
$RPM_BUILD_ROOT%{_prefix}/bin/xgui

cd $RPM_BUILD_ROOT%{_libdir}/SNNS/tools/bin/pc_linux
for n in *; do
ln -fs ../../lib/SNNS/tools/bin/pc_linux/$n $RPM_BUILD_ROOT%{_prefix}/bin/$n
done

cd $RPM_BUILD_ROOT%{_prefix}/bin
ln -fs xgui snns

cd $RPM_BUILD_ROOT%{_libdir}/SNNS
tar zopxf $RPM_SOURCE_DIR/SNNSinfo-1.03.tar.gz
rm -rf SNNSinfo/UserManual.ps SNNSinfo/Icons/.xvpics
cp -f $RPM_SOURCE_DIR/SNNSv%{version}.Manual.ps.gz SNNSinfo
chown -R root.root SNNSinfo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme*
%config %{_libdir}/SNNS/default.cfg
%{_libdir}/SNNS/help.hdoc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/SNNS/*/bin/pc_linux/*
%attr(755,root,root) %{_libdir}/SNNS/examples

%files doc
%defattr(644,root,root,755)
%docdir %{_libdir}/SNNS/SNNSinfo
%doc %{_libdir}/SNNS/SNNSinfo/*
