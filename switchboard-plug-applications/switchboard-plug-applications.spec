%define rev 103
%define debug_package %{nil}

Summary: Switchboard System Settings Applications Plug
Name: switchboard-plug-applications
Version: 0.1.0.2~rev%{rev}
Release: 1%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-applications

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Application Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang applications-plug


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f applications-plug.lang
%{_libdir}/switchboard/personal/pantheon-applications-plug


%changelog
* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev103-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev102-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev101-1
- omment=Update version tag to represent upstream version.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev101-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev100-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev99-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev98-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev97-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev96-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev95-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev94-1
- Remove no longer installed .desktop file from package spec.

* Fri Sep 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev93-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev92-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev92-1
- Bump to version 0.1.0.1.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev88-1
- Update to new upstream snapshot.

* Mon Jul 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Initial package.


