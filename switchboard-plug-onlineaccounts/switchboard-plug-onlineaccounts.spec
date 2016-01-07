%define rev 256
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
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

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

%{_datadir}/accounts/providers/*
%{_datadir}/accounts/services/*
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service

%{_datadir}/icons/hicolor/scalable/apps/*

%files devel
%{_includedir}/pantheon-online-accounts/
%{_libdir}/pkgconfig/pantheon-online-accounts.pc
%{_libdir}/libpantheon-online-accounts.so

%{_datadir}/vala/vapi/pantheon-online-accounts.deps
%{_datadir}/vala/vapi/pantheon-online-accounts.vapi


%changelog
* Thu Jan 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev256-1
- Update to new upstream snapshot.

* Thu Dec 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev255-1
- Update to new upstream snapshot.

* Tue Dec 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev251-1
- Update to new upstream snapshot.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev250-1
- Update to new upstream snapshot.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev249-1
- Update to new upstream snapshot.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev248-1
- Update to new upstream snapshot.

* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev246-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev245-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev244-2
- Fix build, desktop file got removed.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev244-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev241-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev239-1
- Update to new upstream snapshot.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev238-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev237-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev236-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev235-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev234-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev233-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev232-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev230-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev229-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev228-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev227-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev225-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev224-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev223-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev222-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev221-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev220-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev219-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev218-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev217-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0~rev216-2
- Try to fix f23-x64 build.

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



