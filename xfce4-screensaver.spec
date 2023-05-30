Summary:	Screen saver and locker for Xfce
Name:		xfce4-screensaver
Version:	4.18.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/apps/xfce4-screensaver/4.18/%{name}-%{version}.tar.bz2
# Source0-md5:	b5c0a2ce0dce20cb0297bd106b8a796e
URL:		https://docs.xfce.org/apps/screensaver/start
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	exo-devel
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce Screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hy_AM

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xfce4-screensaver
%{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%attr(755,root,root) %{_bindir}/xfce4-screensaver
%attr(755,root,root) %{_bindir}/xfce4-screensaver-command
%attr(755,root,root) %{_bindir}/xfce4-screensaver-configure
%attr(755,root,root) %{_bindir}/xfce4-screensaver-preferences
%attr(755,root,root) %{_libexecdir}/xfce4-screensaver-dialog
%attr(755,root,root) %{_libexecdir}/xfce4-screensaver-gl-helper
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
