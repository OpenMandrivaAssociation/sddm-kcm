%define date 20131022

Name: sddm-kcm
Summary: Systemsettings module for configuring the SDDM display manager
Version: 0.1
%if %date
Release: 0.%date.1
# Packaged from git for the time being -- no download URL available
Source0: %{name}-%date.tar.xz
%else
Release: 1
%endif
URL: https://github.com/sddm-kcm
Group: Graphical desktop/KDE
License: GPLv2
BuildRequires: pkgconfig(QtCore) pkgconfig(QtGui) pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: kdelibs4-devel kde4-macros
Requires: sddm

%description
Systemsettings module for configuring the SDDM display manager (login screen)

%prep
%setup -q -n %name
%cmake_kde4

%build
cd build
%make

%install
cd build
%makeinstall_std

%files
%{_datadir}/apps/%{name}
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
%{_libdir}/kde4/kcm_sddm.so
%{_libdir}/kde4/libexec/kcmsddm_authhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_datadir}/kde4/services/kcm_sddm.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
