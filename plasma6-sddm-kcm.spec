%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230527

Name: plasma6-sddm-kcm
Summary: Systemsettings module for configuring the SDDM display manager
Version:	5.240.0
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/sddm-kcm/-/archive/master/sddm-kcm-master.tar.bz2#/sddm-kcm-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%endif
Patch0: https://gitweb.frugalware.org/frugalware-current/raw/master/source/plasma/sddm-kcm/dpi-fix.patch
Release:	%{?git:0.%{git}.}1
URL: https://github.com/sddm-kcm
Group: Graphical desktop/KDE
License: GPLv2
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6CoreTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WidgetsTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6KCMUtils)
Requires: plasma6-sddm

%description
Systemsettings module for configuring the SDDM display manager (login screen).

%prep
%autosetup -p1 -n sddm-kcm-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kcm_sddm || touch kcm_sddm.lang

%files -f kcm_sddm.lang
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmsddm.conf
%{_datadir}/knsrcfiles/sddmtheme.knsrc
%{_bindir}/sddmthemeinstaller
%{_libdir}/libexec/kauth/kcmsddm_authhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsddm.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsddm.policy
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_sddm.so
%{_datadir}/applications/kcm_sddm.desktop
