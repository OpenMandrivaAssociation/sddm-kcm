%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define date 0

Name: sddm-kcm
Summary: Systemsettings module for configuring the SDDM display manager
Version: 5.13.1
%if %date
Release: 1.%date.1
# Packaged from git for the time being -- no download URL available
Source0: %{name}-%date.tar.xz
%else
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
Release: 1
%endif
URL: https://github.com/sddm-kcm
Group: Graphical desktop/KDE
License: GPLv2
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: cmake(Qt5Designer)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5Archive)
Requires: sddm

%description
Systemsettings module for configuring the SDDM display manager (login screen).

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm_sddm || touch kcm_sddm.lang

%files -f kcm_sddm.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
%{_sysconfdir}/xdg/sddmtheme.knsrc
%{_bindir}/sddmthemeinstaller
%{_libdir}/qt5/plugins/kcm_sddm.so
%{_libdir}/libexec/kauth/kcmsddm_authhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_datadir}/kservices5/kcm_sddm.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_datadir}/sddm-kcm
