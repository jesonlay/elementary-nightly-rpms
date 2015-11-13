%define rev 9
%define debug_package %{nil}

Summary: A keyboard indicator for wingpanel
Name: wingpanel-indicator-keyboard
Version: 0.1~rev%{rev}
Release: 2%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-keyboard

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A keyboard indicator for wingpanel.


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang keyboard-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig



%files -f keyboard-indicator.lang
%{_libdir}/wingpanel/libkeyboard.so


%changelog
* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev9-2
- Fix build by including translations.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev9-1
- Update to new upstream snapshot.

* Thu Nov 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev8-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev6-2
- Release bump for wingpanel soname change.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev6-1
- rebuild trigger for granite soname bump

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev6-1
- Update to new upstream snapshot.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev6-1
- Initial package.


