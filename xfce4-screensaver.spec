Summary:	Screen saver and locker for Xfce
Name:		xfce4-screensaver
Version:	0.1.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-screensaver/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	0fea7b676e6e533a3f305c6f642fe0cd
URL:		https://docs.xfce.org/apps/screensaver/start
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	exo-devel
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libsoup-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xfce4-screensaver
/etc/xdg/autostart/xfce4-screensaver.desktop
/etc/xdg/menus/xfce4-screensavers.menu
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
