%define major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		wildmidi
Version:	0.4.0
Release:	3
Summary:	Open Source Midi Sequencer
Group:		Sound
License:	GPLv3+ and LGPLv3+
URL:		http://wildmidi.sourceforge.net
Source0:	https://github.com/Mindwerks/wildmidi/archive/%name-%version.tar.gz
#Patch0:		wildmidi-0.2.3.4-fix-default-config-location.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake
Requires:	timidity-instruments

%description
WildMidi is a software midi play which has a core softsynth
library that can be use with other applications.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.cfg.5*

#------------------------------------------------------------------------------------------------
%package -n %{libname}
Summary: Library for wildmidi
Group: System/Libraries

%description -n %{libname}
This package contains library files for wildmidi

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#------------------------------------------------------------------------------------------------
%package -n %{develname}
Summary:	Development files for wildmidi
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains development files for wildmidi

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/man3/*.3*

#------------------------------------------------------------------------------------------------
%prep
%setup -qn %{name}-%{name}-%{version}
%apply_patches

%build
%cmake
# parallel build fails, so we don't use it
%make

%install
%makeinstall_std -C build
