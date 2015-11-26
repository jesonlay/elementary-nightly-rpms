%define rev 197
%define debug_package %{nil}

Summary: Switchboard System Settings User Accounts Plug
Name: switchboard-plug-useraccounts
Version: 0.1.2~rev%{rev}
Release: 1%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-useraccounts

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub User Accounts Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang useraccounts-plug


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f useraccounts-plug.lang
%{_libdir}/switchboard/system/pantheon-useraccounts/
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.user-accounts.policy


%changelog
* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev197-1
- Update to new upstream snapshot.

* Tue Nov 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev196-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev194-1
- Update to new upstream snapshot.

* Sat Nov 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev193-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev192-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev191-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev190-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev189-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev188-1
- Update to new upstream snapshot.

* Sun Oct 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev187-1
- Update to new upstream snapshot.

* Sat Oct 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev186-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev185-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev184-1
- Update to new upstream snapshot.

* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev182-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev180-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev179-1
- Remove no longer shipped desktop file. Modernize spec.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev177-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev176-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev176-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev175-1
- Initial package.



