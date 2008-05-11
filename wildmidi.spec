%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Name: wildmidi
Version: 0.2.2
Release: %mkrel 2
Summary: WildMidi Open Source Midi Sequencer
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: http://wildmidi.sourceforge.net
Source:	http://dfn.dl.sourceforge.net/sourceforge/wildmidi/%name-%version.tar.gz
BuildRequires: timidity-instruments
BuildRequires: libalsa-devel
Requires: timidity-instruments

%description 
WildMidi is a software midi play which has a core softsynth library that can be use with other applications.

%files
%defattr(-,root,root,-)
%doc README TODO changelog
%{_bindir}/%{name}

#------------------------------------------------------------------------------------------------
%package -n %libname
Summary: Library for wildmidi
Group: System/Libraries

%description -n %libname
This package contains library files for wildmidi

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*

#------------------------------------------------------------------------------------------------
%package -n %develname
Summary: Development files for wildmidi
Group: Development/Other
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %develname
This package contains development files for wildmidi

%files -n %develname
%doc TODO changelog
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*.h

#------------------------------------------------------------------------------------------------
%prep
%setup -q -n %name-%version

%build
%configure2_5x --disable-werror --with-timidity-cfg=/etc/timidity/timidity.cfg
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot
