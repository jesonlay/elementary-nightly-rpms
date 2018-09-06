%global __provides_exclude_from ^%{_libdir}/io.elementary.code/.*\\.so$

%global srcname scratch
%global appname io.elementary.code

Name:           elementary-code
Summary:        The text editor that works
Version:        2.4.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{srcname}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-devel

BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.1
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme

Obsoletes:      scratch-text-editor
Provides:       scratch-text-editor


%description
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

Make it yours. Scratch is written from the ground up to be extensible.
Keep things super lightweight and simple, or install extensions to turn
Scratch into a full-blown IDE; it's your choice. And with a handful of
useful preferences, you can tweak the behavior and interface to your
liking.

It's elementary. Scratch is made to be the perfect text editor for
elementary, meaning it closely follows the high standards of design,
speed, and consistency. It's sexy, but not distracting.

Works with your language. Whether you're crafting code in Vala,
scripting with PHP, or marking things up in HTML, Scratch has you
covered. Experience full syntax highlighting with nearly all
programming, scripting, and markup languages.

Other syntax-highlighted languages: Bash, C, C#, C++. Cmake, CSS,
.Desktop, Diff, Fortran, Gettext, ini, Java, JavaScript, LaTex, Lua,
Makefile, Objective C, Pascal, Perl, Python, Ruby, XML.

Additional features include:

 * syntax highlighting with gtksourceview-3
 * a find bar to search the words in the files
 * strong integration with Granite framework by elementary-team
 * tab and split documents system
 * lots of others

Scratch needs to be translated. Go to Translations to help us providing
this software in your language!


%package        devel
Summary:        The text editor that works
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Scratch is the text editor that works for you. It auto-saves your files,
meaning they're always up-to-date. Plus it remembers your tabs so you
never lose your spot, even in between sessions.

This package contains the development headers.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%ldconfig_scriptlets


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/
%{_libdir}/libcodecore.so.0
%{_libdir}/libcodecore.so.0.0

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/%{appname}/
%{_datadir}/metainfo/%{appname}.appdata.xml

%files devel
%{_includedir}/codecore.h

%{_libdir}/libcodecore.so
%{_libdir}/pkgconfig/codecore.pc

%{_datadir}/vala/vapi/codecore.deps
%{_datadir}/vala/vapi/codecore.vapi


%changelog
* Thu Sep 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180906.000849.74e42c3a-1
- Update to latest snapshot.

* Tue Sep 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180904.000554.7554101b-1
- Update to latest snapshot.

* Sat Sep 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180901.000807.696e2ceb-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.130415.0c6093c6-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.115906.a265f9f2-1
- Update to latest snapshot.

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180831.025118.92086580-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.194029.27fecd61-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.182358.6e69e299-1
- Update to latest snapshot.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.054758.6c46c77b-2
- Adapt to upstream dependency changes.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180829.054758.6c46c77b-1
- Update to latest snapshot.

* Mon Aug 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180826.000409.df6691cb-1
- Update to latest snapshot.

* Thu Aug 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180823.170549.24b4a60f-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180820.211957.477faeae-1
- Update to latest snapshot.

* Mon Aug 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180820.174319.e55d48c4-1
- Update to latest snapshot.

* Sun Aug 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180819.000847.98e6edea-1
- Update to latest snapshot.

* Sat Aug 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180818.134306.275970c6-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.150514.7d984752-1
- Update to latest snapshot.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-3
- Fix building by being less smart.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-2
- Occasional mass rebuild.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180816.031621.591cb429-1
- Update to latest snapshot.

* Tue Aug 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180813.000248.959b5715-2
- Adapt to libvala bump.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180813.000248.959b5715-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180812.112418.4c9c72f8-1
- Update to latest snapshot.

* Sun Aug 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180812.000533.02084e1a-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180809.125811.5b7fbfda-1
- Update to latest snapshot.

* Thu Aug 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180809.000504.3b318b31-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.151542.322c2eec-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.135615.608fcae3-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.091545.1439bb9d-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.080835.12a5e22a-1
- Update to latest snapshot.

* Wed Aug 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180808.062727.911932b0-1
- Update to latest snapshot.

* Fri Aug 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180803.000350.d3a45b28-1
- Update to latest snapshot.

* Thu Aug 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180802.181951.8c5f17da-1
- Update to latest snapshot.

* Tue Jul 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180731.223701.e0004a34-1
- Update to latest snapshot.

* Mon Jul 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180730.000718.a62fa1ea-1
- Update to latest snapshot.

* Sun Jul 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180722.000325.07b93fd1-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.190302.8cf17e8b-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.121900.83ee0290-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.104145.60be3c97-1
- Update to latest snapshot.

* Sat Jul 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180721.000707.f5cd46f4-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180720.111147.63e4f159-1
- Update to latest snapshot.

* Fri Jul 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180720.000650.3ff1e5c8-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180719.170336.a28ca0d0-1
- Update to latest snapshot.

* Thu Jul 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180719.000331.17b6ff9f-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.185919.91033659-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.122448.b000917b-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.101018.8870817d-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.082404.afe66381-1
- Update to latest snapshot.

* Wed Jul 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180718.073221.6fd4b53b-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180717.183506.7c281376-1
- Update to latest snapshot.

* Tue Jul 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180717.173400.b277fda3-1
- Update to latest snapshot.

* Sun Jul 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180715.000959.e90959dc-1
- Update to latest snapshot.

* Fri Jul 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180713.000329.d3492b37-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180710.143312.12e5dd6a-1
- Update to latest snapshot.

* Tue Jul 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180710.000325.78d6a211-1
- Update to latest snapshot.

* Sat Jul 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180706.000757.d147cbec-2
- Adapt to upstream file changes.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180706.000757.d147cbec-1
- Update to latest snapshot.

* Thu Jul 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180704.210827.bcefca30-1
- Update to latest snapshot.

* Wed Jul 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180703.000557.6d626625-1
- Update to latest snapshot.

* Fri Jun 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180615.001000.737256ff-1
- Update to latest snapshot.

* Thu Jun 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180614.000708.9a4a16ea-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.152600.0d8de916-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.121936.b566cec3-1
- Update to latest snapshot.

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180613.000241.3c1cb848-1
- Update to latest snapshot.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180612.162950.a24e9566-1
- Update to latest snapshot.

* Sun Jun 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180610.001105.6e22c031-1
- Update to latest snapshot.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180608.001112.14471ee3-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180606.205953.6a5cc8fd-1
- Update to latest snapshot.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180606.000759.60471b55-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180605.092434.5bdc20c9-1
- Update to latest snapshot.

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180605.000521.bc6e2d91-1
- Update to latest snapshot.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180604.000827.df6bc66e-1
- Update to latest snapshot.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180603.162531.d1618141-1
- Update to latest snapshot.

* Sat Jun 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180602.000435.f63a2d78-1
- Update to latest snapshot.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180601.000652.06bd1c68-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.150917.46f6cee7-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.144958.ca362b18-1
- Update to latest snapshot.

* Thu May 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180531.000206.372c3b67-1
- Update to latest snapshot.

* Tue May 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180529.001104.68360211-1
- Update to latest snapshot.

* Mon May 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180528.123800.b237d932-1
- Update to latest snapshot.

* Sun May 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180527.000443.47159cf0-1
- Update to latest snapshot.

* Sat May 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180526.073944.9cfeffa8-1
- Update to latest snapshot.

* Thu May 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180524.160358.21d512a8-1
- Update to latest snapshot.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180518.082357.0c987928-1
- Update to latest snapshot.

* Thu May 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180517.000131.1160c09a-1
- Update to latest snapshot.

* Wed May 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180516.184432.86040600-1
- Update to latest snapshot.

* Tue May 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180515.000540.f25153e8-1
- Update to latest snapshot.

* Mon May 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180514.145252.dc765970-1
- Update to latest snapshot.

* Sat May 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180512.001056.370e422d-1
- Update to latest snapshot.

* Fri May 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180511.061657.4d0fc620-1
- Update to latest snapshot.

* Thu May 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180510.064254.d3effc13-1
- Fix build due to bogus changelog entries.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180421.162355.9329bf5b-1
- Update to latest snapshot.

* Sun Apr 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180421.001026.9209d900-1
- Update to latest snapshot.

* Fri Apr 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180420.001116.92d67c54-1
- Update to latest snapshot.

* Thu Apr 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180419.172746.ca7a24f6-1
- Update to latest snapshot.

* Tue Apr 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180417.183345.622afc32-1
- Update to latest snapshot.

* Mon Apr 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180416.000339.13d09286-1
- Update to latest snapshot.

* Sun Apr 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180415.171917.abac84b8-1
- Update to latest snapshot.

* Tue Apr 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180403.000528.88639b83-1
- Update to latest snapshot.

* Wed Mar 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180328.000336.2d04e755-1
- Update to latest snapshot.

* Tue Mar 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180327.000137.86513d03-1
- Update to latest snapshot.

* Mon Mar 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180326.072358.fefa07b2-1
- Update to latest snapshot.

* Sun Mar 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180324.151817.64db28f9-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.191347.8ff356a4-1
- Update to latest snapshot.
- Adapt to upstream dependency changes.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.185628.7ea0aac1-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.134356.17216658-1
- Update to latest snapshot.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180322.021758.e59a69a2-1
- Update to latest snapshot.

* Wed Mar 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180321.160405.0a830c14-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.191932.91728fda-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.182241.89dd92f5-1
- Update to latest snapshot.

* Tue Mar 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180320.034656.d06bc802-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.225618.af5b02ea-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.204714.6f545742-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.182316.4eb6bf78-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.155402.0a03186c-1
- Update to latest snapshot.

* Mon Mar 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180319.000143.c263fa22-1
- Update to latest snapshot.

* Sun Mar 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180318.014452.600d44ae-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.225504.5197da96-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.193317.53c41de6-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.101513.e0a7cdc9-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.091702.61f4b86b-1
- Update to latest snapshot.

* Sat Mar 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180317.001124.40c0b8b3-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180316.182314.a4212caa-1
- Update to latest snapshot.

* Fri Mar 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180316.004052.b29a98a5-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180315.180805.2e970910-1
- Update to latest snapshot.

* Thu Mar 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180315.004730.9a1b77ca-1
- Update to latest snapshot.

* Wed Mar 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180314.000156.e16b5795-1
- Update to latest snapshot.

* Tue Mar 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180312.202140.d65721e2-1
- Update to latest snapshot.

* Sat Mar 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180310.000330.a44720c2-1
- Update to latest snapshot.

* Fri Mar 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180309.112149.a400d30b-1
- Update to latest snapshot.

* Wed Mar 07 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180307.000931.3fe16b80-1
- Update to latest snapshot.

* Tue Mar 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180306.000445.5b84a413-1
- Update to latest snapshot.

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180304.000738.1c5e17af-1
- Update to latest snapshot.

* Thu Mar 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180301.000317.1599c6fa-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180227.185938.5312a6a6-1
- Update to latest snapshot.

* Tue Feb 27 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180227.000356.827a5d89-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180226.105909.8b98c54e-1
- Update to latest snapshot.

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180225.165330.c726d965-1
- Update to latest snapshot.

* Sun Feb 25 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180225.023324.d7ef7e5d-1
- Update to latest snapshot.

* Sat Feb 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180224.115243.1a4af761-1
- Update to latest snapshot.

* Fri Feb 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180223.181222.6e77ae1b-1
- Update to latest snapshot.

* Thu Feb 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180222.000758.26f3b776-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.143240.251c99b9-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.123443.c8e53c66-1
- Update to latest snapshot.

* Wed Feb 21 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180221.074128.83155730-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180220.192202.59278f0c-1
- Update to latest snapshot.

* Tue Feb 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180220.022714.e305f284-1
- Update to latest snapshot.

* Mon Feb 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180219.175143.82a1697f-1
- Update to latest snapshot.

* Sun Feb 18 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180218.145615.edc1200c-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180216.125400.069696a9-1
- Update to latest snapshot.

* Fri Feb 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180216.000253.9691592b-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180214.182858.2d3f62bd-1
- Update to latest snapshot.

* Wed Feb 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180214.013747.b4951d12-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180213.213524.e3686e34-1
- Update to latest snapshot.

* Tue Feb 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180213.005517.891c74fa-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.212015.b3353b8f-1
- Update to latest snapshot.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.160234.0954ba6d-2
- Adapt to cmake -> meson switch.

* Mon Feb 12 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180212.160234.0954ba6d-1
- Update to latest snapshot.

* Fri Feb 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180209.001000.2d369a0a-1
- Update to latest snapshot.

* Tue Feb 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180206.200848.714fc767-1
- Update to latest snapshot.

* Wed Jan 31 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.195832.b8629598-2
- Be lazy about undefined symbols in plugins.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.195832.b8629598-1
- Update to latest snapshot.

* Mon Jan 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180129.185322.b15ff49d-1
- Update to latest snapshot.

* Sun Jan 28 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180125.000833.ad688fc4-1
- Update to latest snapshot.

* Wed Jan 24 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180124.123947.d3ab6ba9-1
- Update to latest snapshot.

* Tue Jan 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180123.221341.4969d443-1
- Update to latest snapshot.

* Mon Jan 22 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180122.060359.dc426bee-1
- Update to latest snapshot.

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180120.020812.e959a13c-1
- Update to latest snapshot.

* Wed Jan 17 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180117.192407.07d814d5-1
- Update to latest snapshot.

* Tue Jan 16 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180116.180121.cc9cd0ba-1
- Update to latest snapshot.

* Mon Jan 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180112.191811.9961a070-1
- Update to latest snapshot.

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180111.160157.63bf2a42-1
- Update to latest snapshot.

* Wed Jan 10 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.231632.616f30af-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.222901.cefbdb61-1
- Update to latest snapshot.

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180109.170232.0d7cbb8a-1
- Update to latest snapshot.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-2
- Adapt to upstream file changes.

* Mon Jan 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180108.201726.899b0b68-1
- Update to latest snapshot.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-2
- Remove icon cache scriptlets.

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180106.000312.b62cbf36-1
- Update to latest snapshot.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180105.001608.fc57a13d-1
- Update to latest snapshot.

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git171219.151614.17101d60-1
- Initial package.


