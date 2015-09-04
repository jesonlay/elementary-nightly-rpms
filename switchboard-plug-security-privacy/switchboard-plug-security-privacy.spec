%define rev 185
%define debug_package %{nil}

Summary: Switchboard System Settings Security and Privacy Plug
Name: switchboard-plug-security-privacy
Version: 0.1.0.1~rev%{rev}
Release: 2%{?dist}
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
%{_datadir}/applications/pantheon-security-privacy-plug.desktop
%{_datadir}/polkit-1/actions/org.pantheon.security-privacy.policy


%changelog
* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev185-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev185-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev184-1
- Initial package.



