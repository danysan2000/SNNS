
Summary:	Stuttgart Neural Network Simulator
Summary(pl):	Sztutgardzki symulator sieci neuronowych
Name:		SNNS
Version:	4.2
Release:	1.0
License:	Free Software
Group:		X11/Applications
Source0:	ftp://ftp.informatik.uni-stuttgart.de/pub/SNNS/%{name}v%{version}.tar.gz
# Source0-md5:	4609dfd61714bfbb0842d4e8e905e584
Source2:	ftp://ftp.informatik.uni-stuttgart.de/pub/SNNS/%{name}v%{version}.Manual.ps.gz
# Source2-md5:	1df5e14726c88d01be9f67e4590600a9
#Source3:	ftp://ftp.informatik.uni-stuttgart.de/pub/SNNS/%{name}info-1.03.tar.gz
# Source3-md5:	c2a99f0294bd02e5f3bfdff6bf16469a
Source4:        %{name}.desktop
Patch0:		%{name}-include.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-XGUILOADPATH.diff
Patch3:		%{name}-inc_fix.patch
URL:		http://www.informatik.uni-stuttgart.de/ipvr/bv/projekte/snns/snns.html
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SNNS (Stuttgart Neural Network Simulator) is a neuron network
simulator.

%description -l de
SNNS (Stuttgart Neural Network Simulator) ist ein Simulationsprogramm
für Neuronal Netzwerk.

%description -l pl
SNNS (Stuttgart Neural Network Simulator) jest symulatorem sieci
neuronowych.

%package doc
Summary:	SNNS documentation
Summary(de):	SNNS-Dokomentationen
Summary(pl):	Dokumentacja do SNNS
Group:		X11/Applications

%description doc
Documentation for SNNS in HTML and postscript.

%description doc -l de
Dieses Paket enthält die Dokumentationen in HTML und
Postscript-Format.

%description doc -l pl
Ten pakiet zawiera dokumentacjê w HTML-u i postscripcie.

%prep
%setup -q -n %{name}v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure2_13 \
	--enable-global
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_mandir}/man1,%{_desktopdir}}

%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

cp -af help.hdoc default.cfg examples $RPM_BUILD_ROOT%{_libdir}/%{name}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} .
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}

gunzip %{name}v%{version}.Manual.ps.gz

cd $RPM_BUILD_ROOT%{_bindir}
ln -fs xgui snns

#cd $RPM_BUILD_ROOT%{_libdir}/SNNS
#tar zopxf $RPM_SOURCE_DIR/SNNSinfo-1.03.tar.gz
#rm -rf SNNSinfo/UserManual.ps SNNSinfo/Icons/.xvpics
#cp -f $RPM_SOURCE_DIR/SNNSv%{version}.Manual.ps.gz SNNSinfo
#chown -R root.root SNNSinfo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme* 
%config %{_libdir}/%{name}/default.cfg
%{_libdir}/%{name}/help.hdoc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/examples
%{_mandir}/man1/*
%{_desktopdir}/*

%files doc
%defattr(644,root,root,755)
%docdir %{_libdir}/SNNS/SNNSinfo
%doc tools/doc/* %{name}v%{version}.Manual.ps
#%doc %{_libdir}/SNNS/SNNSinfo/*
