Summary:	Screen saver and locker for Xfce
Name:		xfce4-screensaver
Version:	4.20.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-screensaver/4.20/%{name}-%{version}.tar.xz
# Source0-md5:	cbd8bdb0c5e95fe1eab042c8066294f1
URL:		https://docs.xfce.org/apps/screensaver/start
BuildRequires:	dbus-devel >= 1.9.2
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	garcon-devel >= 4.16.0
BuildRequires:	garcon-gtk3-devel >= 4.16.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libwnck-devel >= 3.20
BuildRequires:	libxfce4ui-devel >= 4.18.4
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	libxfce4windowing-devel >= 4.19.2
BuildRequires:	libxklavier-devel >= 5.2
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	wayland-devel >= 1.15
BuildRequires:	wayland-protocols >= 1.20
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
BuildRequires:	xorg-lib-libX11-devel >= 1.6.7
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel >= 1.2.3
BuildRequires:	xorg-lib-libXext-devel >= 1.0.0
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce Screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,hy_AM}
%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xfce4-screensaver
%{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%attr(755,root,root) %{_bindir}/xfce4-screensaver
%attr(755,root,root) %{_bindir}/xfce4-screensaver-command
%attr(755,root,root) %{_prefix}/libexec/xfce4-screensaver-configure.py
%attr(755,root,root) %{_bindir}/xfce4-screensaver-preferences
%attr(755,root,root) %{_libexecdir}/xfce4-screensaver-dialog
%dir %{_libexecdir}/xfce4-screensaver
%attr(755,root,root) %{_libexecdir}/xfce4-screensaver/floaters
%attr(755,root,root) %{_libexecdir}/xfce4-screensaver/popsquares
%attr(755,root,root) %{_libexecdir}/xfce4-screensaver/slideshow
%{_desktopdir}/screensavers/xfce-floaters.desktop
%{_desktopdir}/screensavers/xfce-personal-slideshow.desktop
%{_desktopdir}/screensavers/xfce-popsquares.desktop
%{_desktopdir}/xfce4-screensaver-preferences.desktop
%{_datadir}/dbus-1/services/org.xfce.ScreenSaver.service
%{_datadir}/desktop-directories/xfce4-screensaver.directory
%{_mandir}/man1/xfce4-screensaver-command.1*
%{_mandir}/man1/xfce4-screensaver-preferences.1*
%{_mandir}/man1/xfce4-screensaver.1*
%{_pixmapsdir}/xfce-logo-white.svg
%{_iconsdir}/hicolor/*/apps/org.xfce.ScreenSaver.*
