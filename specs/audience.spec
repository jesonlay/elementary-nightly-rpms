Summary:        Audience video player
Name:           audience
Version:        0.2.1.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/audience

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
# BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 0.3.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)


%description
A modern video player that brings the lessons learned from the web home
to the desktop.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang audience


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
# appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files       -f audience.lang
%doc AUTHORS README
%license COPYING

%{_bindir}/audience

%{_datadir}/appdata/org.pantheon.audience.appdata.xml
%{_datadir}/applications/org.pantheon.audience.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.audience.gschema.xml


%changelog
* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev703-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev701-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev700-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev699-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev698-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev697-1
- Update to latest snapshot.

* Tue Nov 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev696-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev695-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev694-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev693-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev692-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev691-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1.1+rev690-1
- Update to version 0.2.1.1.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev690-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev689-1
- Update to latest snapshot.

* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev688-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev687-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev686-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev685-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev684-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev682-1
- Update to latest snapshot.

* Fri Oct 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev681-1
- Update to latest snapshot.

* Sun Oct 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev680-1
- Update to latest snapshot.

* Sat Oct 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev679-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev678-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev677-2
- Spec file cleanups.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev677-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev676-2
- Disable appdata validation for now.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev676-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev675-2
- Spec file cosmetics.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev675-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev674-1
- Update to latest snapshot.

* Tue Sep 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev671-1
- Update to latest snapshot.

* Mon Sep 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev670-1
- Update to latest snapshot.

* Sun Sep 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev669-1
- Update to latest snapshot.

* Sun Sep 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev668-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev665-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev663-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev659-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev658-1
- Update to latest snapshot.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2+rev656-1
- Update to version 0.2.0.2.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.2~rev655-1
- Update to version 0.2.0.2.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.1~rev655-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.1~rev654-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.1~rev653-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.1~rev652-1
- Update to version 0.2.0.1.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev651-1
- Update to latest snapshot.

* Fri Sep 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev650-1
- Update to latest snapshot.

* Tue Sep 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev648-1
- Update to latest snapshot.

* Mon Sep 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev647-1
- Update to latest snapshot.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev646-1
- Update to latest snapshot.

* Sat Sep 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev645-1
- Update to latest snapshot.

* Fri Sep 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev644-1
- Update to latest snapshot.

* Thu Sep 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev643-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev642-1
- Update to latest snapshot.

* Sun Aug 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev641-1
- Update to latest snapshot.

* Sun Aug 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev640-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev639-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev638-1
- Update to latest snapshot.

* Wed Aug 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev637-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev633-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2~rev632-1
- Update to version 0.2.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev631-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev630-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev629-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev628-1
- Update to latest snapshot.

* Tue Aug 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev627-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev626-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev625-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev623-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev623-1
- Update to latest snapshot.

* Sat Aug 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev621-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev620-4
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt spec to upstream appdata file name change.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev620-3
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Adapt spec to upstream .desktop file name change.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev620-2
- Update for packaging changes.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com>
- Add BR: intltool to fix build.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev620-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev619-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev616-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev609-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev606-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev605-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev604-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev603-1
- Update to latest snapshot.

* Fri Jul 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev602-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev601-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev600-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev599-1
- Update to latest snapshot.

* Fri Jul 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev598-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev597-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev596-1
- Update to latest snapshot.

* Wed Jul 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev595-1
- Update to latest snapshot.

* Wed Jul 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev594-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev593-2
- Update for packaging changes.

* Fri Jun 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev589-1
- Update to latest snapshot.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev588-1
- Update to latest snapshot.

* Thu Jun 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev587-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev586-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev585-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev584-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev584-2
- Update for packaging changes.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev584-1
- Update to latest snapshot.

* Thu May 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev583-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev582-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev581-1
- Update to latest snapshot.

* Wed May 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev581-1
- Update to latest snapshot.

* Mon May 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev580-2
- Update for packaging changes.

* Sat Apr 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev580-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev579-1
- Update to new upstream snapshot.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev578-2
- Add BR: clutter-gst-3.0.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev578-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev576-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev575-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev574-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev573-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev571-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev570-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev569-1
- Update to new upstream snapshot.

* Sat Jan 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev568-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev567-1
- Update to new upstream snapshot.

* Fri Dec 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev566-1
- Update to new upstream snapshot.

* Thu Dec 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev565-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev564-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev563-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev562-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev561-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev560-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev559-2
- Modernise spec. Fix build by including new appdata file. Validate desktop and
  appdata file.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev559-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev556-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev554-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev553-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev552-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev551-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev550-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev549-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev548-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev547-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev546-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev545-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev544-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev543-1
- Update to new upstream snapshot.

* Thu Oct 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev541-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev540-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev539-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev538-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev537-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev536-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev535-2
- rebuild trigger for granite soname bump

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.2~rev535-1
- Update to new upstream snapshot.

* Sun Aug 16 2015 Fabio Valentini - 0.1.0.2~rev534-1
- Bump to correct upstream version (0.1.0.2).

* Sun Aug 16 2015 Fabio Valentini - 0.1.0.1~rev534-1
- Update to upstream bzr snapshot revno 534.

* Wed Jul 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev531-1
- Update to bzr snapshot revno 531.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev529-2
- Use %doc and %license macros.

* Fri Jul 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev529-1
- Update to bzr snapshot revno 529.
- Use more spec macros.

* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev498-5
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev485-4
- Update to latest bzr snapshot.

* Sun Jan 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev482-3
- Update to latest bzr snapshot.

* Thu Jan 08 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev481-2
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev479-1
- Update to bzr revision 479.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.1~rev477-1
- Initial package.


