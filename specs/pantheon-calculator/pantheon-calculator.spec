Summary:        A tiny, simple calculator written in GTK+ and Vala.
Name:           pantheon-calculator
Version:        0.1.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-calculator

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
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
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%files -f pantheon-calculator.lang
%doc AUTHORS
%license COPYING

%{_bindir}/pantheon-calculator

%{_datadir}/appdata/org.pantheon.calculator.appdata.xml
%{_datadir}/applications/org.pantheon.calculator.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.calculator.gschema.xml


%changelog
* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev310-1
- Update to latest snapshot.

* Sat Jan 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev309-1
- Update to version 0.1.1.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev308-1
- Update to version 0.1.1.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev307-1
- Update to version 0.1.1.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev306-1
- Update to version 0.1.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev305-1
- Update to version 0.1.1.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev304-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev303-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev302-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev301-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev300-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev299-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev298-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev297-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev296-1
- Update to latest snapshot.

* Mon Dec 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev295-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev294-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev293-1
- Update to latest snapshot.

* Sat Nov 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev292-1
- Update to latest snapshot.

* Fri Nov 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev291-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev290-1
- Update to latest snapshot.

* Sun Oct 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev289-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev288-1
- Update to latest snapshot.

* Wed Oct 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev287-1
- Update to latest snapshot.

* Tue Oct 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev286-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev285-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev284-2
- Spec file cleanups.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev284-1
- Update to latest snapshot.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev283-1
- Update to version 0.1.1.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev282-1
- Update to latest snapshot.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev281-1
- Update to latest snapshot.

* Sun Sep 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev280-1
- Update to latest snapshot.

* Sat Sep 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev279-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev278-2
- Update for packaging changes.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt spec for renamed appdata and desktop files.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev278-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev277-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev275-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev274-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev273-1
- Update to latest snapshot.

* Sat Sep 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev272-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev271-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev270-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev269-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev268-1
- Update to latest snapshot.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev267-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev266-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev265-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev264-1
- Update to version 0.1.1.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev263-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev262-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev261-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev260-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev260-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev259-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev258-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev257-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev254-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev253-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev252-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev251-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev250-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev249-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev248-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev246-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev245-1
- Update to latest snapshot.

* Sun Jul 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev244-1
- Update to latest snapshot.

* Sat Jul 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev243-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev242-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev241-2
- Update for packaging changes.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev237-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev236-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev235-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev234-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev233-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev232-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev231-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev230-2
- Enable desktop file validation.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev230-1
- Update to latest snapshot.

* Thu Jun 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev229-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev227-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev227-2
- Update for packaging changes.

* Sat May 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev227-1
- Update to latest snapshot.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev226-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev225-1
- Update to latest snapshot.

* Tue May 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev221-1
- Update to latest snapshot.

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev220-1
- Update to latest snapshot.

* Fri May 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev219-1
- Update to latest snapshot.

* Thu May 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev218-1
- Update to latest snapshot.

* Wed May 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev217-1
- Update to latest snapshot.

* Tue May 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev216-1
- Update to latest snapshot.

* Tue May 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev215-1
- Update to latest snapshot.

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


