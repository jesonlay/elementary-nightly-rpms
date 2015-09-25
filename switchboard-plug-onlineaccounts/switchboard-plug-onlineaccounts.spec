%define rev 216
%define debug_package %{nil}

Summary: Switchboard System Settings Online Accounts Plug
Name: switchboard-plug-onlineaccounts
Version: 0.2.0~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-onlineaccounts

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gsignond)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libaccounts-glib)
BuildRequires: pkgconfig(libgsignon-glib)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(rest-0.7)
BuildRequires: pkgconfig(switchboard-2.0)
BuildRequires: pkgconfig(webkit2gtk-4.0)

Requires: hicolor-icon-theme


%description
Modular Desktop Settings Hub Online Accounts Plug


%package devel
Summary: Switchboard System Settings Online Accounts Plug development headers
%description devel
Modular Desktop Settings Hub Online Accounts Plug (development headers)


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-online-accounts


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-onlineaccounts.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%post devel
%postun devel


%files -f pantheon-online-accounts.lang
%{_libdir}/libpantheon-online-accounts.so.0
%{_libdir}/libpantheon-online-accounts.so.0.1

%{_libdir}/pantheon-online-accounts/
%{_libdir}/switchboard/network/pantheon-online-accounts/

%{_datadir}/accounts/

%{_datadir}/applications/pantheon-plug-onlineaccounts.desktop
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service

%{_datadir}/icons/hicolor/scalable/apps/facebook.svg
%{_datadir}/icons/hicolor/scalable/apps/fastmail.svg
%{_datadir}/icons/hicolor/scalable/apps/google.svg
%{_datadir}/icons/hicolor/scalable/apps/microsoft.svg
%{_datadir}/icons/hicolor/scalable/apps/yahoo.svg



%files devel
%{_includedir}/pantheon-online-accounts/
%{_libdir}/pkgconfig/pantheon-online-accounts.pc
%{_libdir}/libpantheon-online-accounts.so

%{_datadir}/vala/vapi/pantheon-online-accounts.deps
%{_datadir}/vala/vapi/pantheon-online-accounts.vapi


%changelog
* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev216-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev213-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev208-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev205-1
- rebuild trigger for granite soname bump

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev205-1
- Initial package.



