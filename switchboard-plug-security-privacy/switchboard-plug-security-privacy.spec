%define rev 198
%define debug_package %{nil}

Summary: Switchboard System Settings Security and Privacy Plug
Name: switchboard-plug-security-privacy
Version: 0.1.0.2~rev%{rev}
Release: 1%{?dist}
License: LGPLv2.1, LGPLv3
URL: http://launchpad.net/switchboard-plug-security-privacy

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(switchboard-2.0)
BuildRequires: pkgconfig(zeitgeist-2.0)


%description
Modular Desktop Settings Hub Security and Privacy Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-security-privacy-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-security-privacy.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-security-privacy-plug.lang
%{_libdir}/switchboard/personal/pantheon-security-privacy/
#%{_datadir}/applications/pantheon-security-privacy-plug.desktop
%{_datadir}/polkit-1/actions/org.pantheon.security-privacy.policy


%changelog
* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev198-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev197-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev196-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev195-1
- Update version tag to represent upstream version.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev195-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev194-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev193-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev192-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev191-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev190-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev189-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev188-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev187-1
- Remove no longer shipped desktop file. Modernize spec.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev185-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev185-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev184-1
- Initial package.



