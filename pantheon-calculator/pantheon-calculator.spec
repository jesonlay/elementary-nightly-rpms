%define rev 158

Summary: A tiny, simple calculator written in GTK+ and Vala.
Name: pantheon-calculator
Version: 0.1.0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/pantheon-calculator

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.11.6


#Requires: contractor


%description
A tiny, simple calculator written in GTK+ and Vala.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-calculator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-calculator.lang
%doc AUTHORS
%license COPYING

%{_bindir}/pantheon-calculator
%{_datadir}/applications/pantheon-calculator.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.calculator.gschema.xml


%changelog
* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev158-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev155-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev154-1
- Initial package.



