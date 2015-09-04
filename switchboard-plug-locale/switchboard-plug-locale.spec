%define rev 155
%define debug_package %{nil}

Summary: Switchboard System Settings Locale Plug
Name: switchboard-plug-locale
Version: 0.2~rev%{rev}
Release: 1%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-locale

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Locale Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang locale-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-locale.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f locale-plug.lang
%{_libdir}/switchboard/personal/pantheon-locale
%{_datadir}/applications/pantheon-plug-locale.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.plug.locale.gschema.xml
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.locale.policy


%changelog
* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev155-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev154-2
- rebuild trigger for granite soname bump

* Sat Aug 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev154-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev153-1
- Initial package.



