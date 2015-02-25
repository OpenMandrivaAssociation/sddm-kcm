%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define date 0

Name: sddm-kcm
Summary: Systemsettings module for configuring the SDDM display manager
Version: 5.2.1
%if %date
Release: 1.%date.1
# Packaged from git for the time being -- no download URL available
Source0: %{name}-%date.tar.xz
%else
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Release: 1
%endif
URL: https://github.com/sddm-kcm
Group: Graphical desktop/KDE
License: GPLv2
BuildRequires: pkgconfig(Qt5Core) pkgconfig(Qt5Gui) pkgconfig(Qt5Declarative)
BuildRequires: pkgconfig(Qt5DBus) pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(xcursor)
BuildRequires: ninja cmake extra-cmake-modules5
Requires: sddm

%description
Systemsettings module for configuring the SDDM display manager (login screen)

%prep
%setup -q
%cmake -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install
%find_lang kcm_sddm

%files -f kcm_sddm.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
%{_libdir}/qt5/plugins/kcm_sddm.so
%{_libdir}/libexec/kauth/kcmsddm_authhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_datadir}/kservices5/kcm_sddm.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_datadir}/sddm-kcm
