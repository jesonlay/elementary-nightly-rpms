Summary:        A tiny, simple calculator written in GTK+ and Vala.
Name:           pantheon-calculator
Version:        0.1.0.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-calculator

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6


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


%check
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-calculator.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f pantheon-calculator.lang
%doc AUTHORS
%license COPYING

%{_bindir}/pantheon-calculator

%{_datadir}/appdata/pantheon-calculator.appdata.xml
%{_datadir}/applications/pantheon-calculator.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.calculator.gschema.xml


%changelog
* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev213-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev213-2
- Update for packaging changes.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev213-1
- Update to new upstream snapshot.

* Sun May 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev212-1
- Update to new upstream snapshot.

* Sat Apr 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev211-1
- Update to new upstream snapshot.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev210-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev209-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev207-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev206-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev205-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev204-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev203-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev201-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev200-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev199-1
- Update to new upstream snapshot.

* Sat Jan 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev198-1
- Update to new upstream snapshot.

* Wed Jan 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev197-1
- Update to new upstream snapshot.

* Thu Jan 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev196-1
- Update to new upstream snapshot.

* Tue Jan 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev195-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev194-1
- Update to new upstream snapshot.

* Sun Jan 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev193-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev192-2
- Add appdata file.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev192-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev190-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev189-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev188-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev187-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev186-1
- Update to new upstream snapshot.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev185-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev184-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev183-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev182-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev180-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev179-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev178-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev177-1
- Update to new upstream snapshot.

* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev176-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev175-1
- Update to new upstream snapshot.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev174-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev173-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev172-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev171-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev170-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev169-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev168-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev166-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev165-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev164-1
- Update to new upstream snapshot.

* Wed Sep 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev162-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev160-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev159-2
- rebuild trigger for granite soname bump

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev159-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev158-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev155-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev154-1
- Initial package.



