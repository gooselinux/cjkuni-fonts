%define fontname cjkuni
%define common_desc \
CJK Unifonts are Unicode TrueType fonts derived from original fonts made \
available by Arphic Technology under "Arphic Public License" and extended by \
the CJK Unifonts project.

%define umingdir         %{_datadir}/fonts/cjkuni-uming
%define ukaidir          %{_datadir}/fonts/cjkuni-ukai

%define gsdir            %{_datadir}/ghostscript/conf.d
%define catalogue        %{_sysconfdir}/X11/fontpath.d

%define umingbuilddir    %{fontname}-uming-fonts-%{version}
%define ukaibuilddir     %{fontname}-ukai-fonts-%{version}

%define _transdir        %{_datadir}/fonts/cjkunifonts-
%define umingtransdir    %{_transdir}uming
%define ukaitransdir     %{_transdir}ukai

Name:        %{fontname}-fonts
Version:     0.2.20080216.1
Release:     34%{?dist}
Summary:     Chinese Unicode TrueType fonts in Ming and Kai face
License:     Arphic
Group:       User Interface/X
URL:         http://www.freedesktop.org/wiki/Software/CJKUnifonts

Source1:    http://ftp.debian.org/debian/pool/main/t/ttf-arphic-uming/ttf-arphic-uming_%{version}.orig.tar.gz
Source2:    http://ftp.debian.org/debian/pool/main/t/ttf-arphic-ukai/ttf-arphic-ukai_%{version}.orig.tar.gz
Source3:    FAPIcidfmap.zh_TW
Source4:    FAPIcidfmap.zh_CN
Source5:    cidfmap.zh_TW
Source6:    cidfmap.zh_CN
Source7:    CIDFnmap.zh_TW
Source8:    CIDFnmap.zh_CN
Patch1:     cjkunifonts-0.2.20080216.1-2.patch
Patch2:     cjkuni-fonts-0.2.20080216.1-18.patch
Patch3:     cjkuni-fonts-0.2.20080216.1-19.patch
Patch4:     cjkuni-fonts-uming-use-latin.patch

BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils, ttmkfdir

%description
%common_desc

%package -n %{fontname}-fonts-common
Summary:      Common package of CJK Unifonts
Group:        User Interface/X
Obsoletes:    cjkunifonts-common <= 0.2.20080216.1-19

%description -n %{fontname}-fonts-common
%common_desc

Common package of CJK Unifonts.

%files -n %{fontname}-fonts-common
%defattr(-,root,root,-)
%dir %{_fontconfig_templatedir}
%dir %{_fontconfig_confdir}

%package -n %{fontname}-uming-fonts
Summary:      Chinese Unicode TrueType font in Ming face
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}
Obsoletes:    cjkunifonts-uming < 0.2.20080216.1-16

%description -n %{fontname}-uming-fonts
%common_desc

CJK Unifonts in Ming face.

%files -n %{fontname}-uming-fonts
%defattr(-,root,root,-)
%doc ../%{umingbuilddir}/license
%doc ../%{umingbuilddir}/CONTRIBUTERS
%doc ../%{umingbuilddir}/Font_Comparison_ShanHeiSun_UMing.odt
%doc ../%{umingbuilddir}/Font_Comparison_ShanHeiSun_UMing.pdf
%doc ../%{umingbuilddir}/FONTLOG
%doc ../%{umingbuilddir}/INSTALL
%doc ../%{umingbuilddir}/KNOWN_ISSUES
%doc ../%{umingbuilddir}/NEWS
%doc ../%{umingbuilddir}/README
#%doc ../%{umingbuilddir}/TODO
%dir %{umingdir}
%{umingdir}/uming.ttc
%{umingdir}/fonts.dir
%{umingdir}/fonts.scale
%{_fontconfig_templatedir}/*-ttf-arphic-uming*.conf
%{_fontconfig_confdir}/*-ttf-arphic-uming*.conf
%{catalogue}/%{name}-uming

%package -n %{fontname}-ukai-fonts
Summary:      Chinese Unicode TrueType font in Kai face
Group:        User Interface/X
Requires:     %{fontname}-fonts-common = %{version}-%{release}
Obsoletes:    cjkunifonts-ukai < 0.2.20080216.1-16

%description -n %{fontname}-ukai-fonts
%common_desc

CJK Unifonts in Kai face.

%files -n %{fontname}-ukai-fonts
%defattr(-,root,root,-)
%doc ../%{ukaibuilddir}/license
%doc ../%{ukaibuilddir}/CONTRIBUTERS
%doc ../%{ukaibuilddir}/Font_Comparison_ZenKai_UKai.odt
%doc ../%{ukaibuilddir}/Font_Comparison_ZenKai_UKai.pdf
%doc ../%{ukaibuilddir}/FONTLOG
%doc ../%{ukaibuilddir}/INSTALL
%doc ../%{ukaibuilddir}/KNOWN_ISSUES
%doc ../%{ukaibuilddir}/NEWS
%doc ../%{ukaibuilddir}/README
%doc ../%{ukaibuilddir}/TODO
%dir %{ukaidir}
%{ukaidir}/ukai.ttc
%{ukaidir}/fonts.dir
%{ukaidir}/fonts.scale
%{_fontconfig_templatedir}/*-ttf-arphic-ukai*.conf
%{_fontconfig_confdir}/*-ttf-arphic-ukai*.conf
%{catalogue}/%{name}-ukai

%package -n %{fontname}-fonts-ghostscript
Summary:      Chinese Unicode TrueType font ghostscript files
Group:        User Interface/X
Requires:     fontpackages-filesystem >= 1.13
Requires:     ghostscript >= 8.63-4
Requires:     %{fontname}-uming-fonts = %{version}-%{release}
Requires:     %{fontname}-ukai-fonts = %{version}-%{release}

%description -n %{fontname}-fonts-ghostscript
%common_desc

CJK Unifonts ghostscript files.

%files -n %{fontname}-fonts-ghostscript
%defattr(-,root,root,-)
%dir %{gsdir}
%{gsdir}/FAPIcidfmap.zh_TW
%{gsdir}/FAPIcidfmap.zh_CN
%{gsdir}/cidfmap.zh_TW
%{gsdir}/cidfmap.zh_CN
%{gsdir}/CIDFnmap.zh_TW
%{gsdir}/CIDFnmap.zh_CN

%prep
%setup -q -c -T -a1 -n %{umingbuilddir}
%patch1 -p1 -b .1-rhbz466667
%patch2 -p1 -b .2-rhbz475743
%patch3 -p1 -b .3-rhbz459680
%patch4 -p0 -b .4-use-latin
%setup -q -c -T -a2 -n %{ukaibuilddir}

%build
%{nil}

%install
%__rm -rf %{buildroot}

# *.ttc(ttf) and font.{dir,scale}
%__install -m 0755 -d %{buildroot}%{umingdir}
%__install -m 0755 -d %{buildroot}%{ukaidir}
%__install -m 0644 ../%{umingbuilddir}/uming.ttc %{buildroot}%{umingdir}/
%__install -m 0644 ../%{ukaibuilddir}/ukai.ttc %{buildroot}%{ukaidir}/

# fonts.{scale,dir} # use upstream included one instead
%__install -m 0644 ../%{umingbuilddir}/fonts.dir %{buildroot}%{umingdir}/
%__install -m 0644 ../%{umingbuilddir}/fonts.scale %{buildroot}%{umingdir}/
%__install -m 0644 ../%{ukaibuilddir}/fonts.dir %{buildroot}%{ukaidir}/
%__install -m 0644 ../%{ukaibuilddir}/fonts.scale %{buildroot}%{ukaidir}/

# *.conf
%__install -m 0755 -d %{buildroot}%{_fontconfig_templatedir}
%__install -m 0755 -d %{buildroot}%{_fontconfig_confdir}
cd ../%{umingbuilddir}
for fconf in `ls *-ttf-arphic-uming*.conf`
do
    %__install -m 0644 $fconf %{buildroot}%{_fontconfig_templatedir}/
    %__ln_s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
cd ../%{ukaibuilddir}
for fconf in `ls *-ttf-arphic-ukai*.conf`
do
    %__install -m 0644 $fconf %{buildroot}%{_fontconfig_templatedir}/
    %__ln_s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
cd -

# ghostscript
%__install -m 0755 -d %{buildroot}%{gsdir}
%__install -m 0644 %{SOURCE3} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE4} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE5} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE6} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE7} %{buildroot}%{gsdir}/
%__install -m 0644 %{SOURCE8} %{buildroot}%{gsdir}/

# catalogue
%__install -m 0755 -d %{buildroot}%{catalogue}
%__ln_s %{umingdir} %{buildroot}%{catalogue}/%{name}-uming
%__ln_s %{ukaidir} %{buildroot}%{catalogue}/%{name}-ukai

%clean
%__rm -fr %{buildroot}

%changelog
* Thu Jan 28 2010 Caius 'kaio' Chance <cchance at redhat.com> - 0.2.20080216.1-34.el6
- Resolves: rhbz#559452
- Fix cjkuni-fonts-common shouls obsoletes cjkunifonts-common instead of itself.

* Thu Jan 28 2010 Caius 'kaio' Chance <cchance at redhat.com> - 0.2.20080216.1-33.el6
- Resolves: rhbz#559452
- Obsolete older version of cjkuni-fonts-common should be done in cjkuni-fonts-common subpackage rather than 
  cjkuni-fonts-ghostscript subpackage.

* Tue Jan 19 2010 Caius 'kaio' Chance <cchance at redhat.com> - 0.2.20080216.1-32.el6
- Resolves: rhbz#556694
- Fix typo.

* Tue Jan 19 2010 Caius 'kaio' Chance <cchance at redhat.com> - 0.2.20080216.1-31.el6
- Resolves: rhbz#556694
- Removes contents of -compat in spec file.
- Removes conflicts tag in -ghostscript.

* Mon Jan 18 2010 Caius 'kaio' Chance <cchance at redhat.com> - 0.2.20080216.1-30.el6
- Resolves: rhbz#556333
- Fixes to rpmlint warnings.

* Thu Jan 14 2010 Caius 'kaio' Chance <cchance at redhat.com> - 0.2.20080216.1-29.el6
- Resolves: rhbz#555216
- Fixes to rpmlint warnings.

* Wed Nov 11 2009 Peng Huang<shawn.p.huang@gmail.com> - 0.2.20080216.1-28
- Use latin font for to display common ascii in Chines string

* Mon Sep 21 2009 Caius 'kaio' Chance <k at kaio.me> - 0.2.20080216.1-27.fc12
- Merged from F-11 tree.
- Obsoleted cjkuni-fonts-common.
- Resolves: rhbz#507637 (using font.{dir,scale} from upstream source)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Caius 'kaio' Chance <cchance@redhat.com> - 0.2.20080216.1-25.fc12
- Rebuilt.

* Fri May 15 2009 Caius 'kaio' Chance <cchance@redhat.com> - 0.2.20080216.1-24.fc12
- Resolves: rhbz#488398 (Fixed ghostscript referred to outdated font location.)

* Wed Apr 08 2009 Caius 'kaio' Chance <cchance@redhat.com> - 0.2.20080216.1-23.fc11
- Resolves: rhbz#483320 (Declared ownership of compatibility directories.)

* Tue Apr 07 2009 Caius 'kaio' Chance <cchance@redhat.com> - 0.2.20080216.1-22.fc11
- Resolves: rhbz#491956.
- Rebuilt for Fedora 11.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-20.fc11
- Resolves: rhbz#483329
- Reowned font directory by -common subpackage.
- Updated font paths in ghostscript files.
- Splited ghostscript files into subpackage.

* Tue Feb 03 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-19.fc11
- Resolves: rhbz#459680
- Disabled antialias when pixelsize is smaller than 17.

* Mon Feb 02 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-18.fc11
- Resolves: rhbz#475743
- Fixed Japanese fonts over-priorized by uming fonts in Japanese locale.

* Thu Jan 22 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-17.fc11
- Resolves: rhbz#477373
- Refined package dependencies and compat font symlinks.

* Wed Jan 21 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-16.fc11
- Resolves: rhbz#253813
- Renamed from cjkunifonts to cjkuni-fonts according to new font packaging
  guidelines.

* Mon Jan 19 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-15.fc11
- Resolves: rhbz#477373
- Updated font renaming for post-1.13 fontpackages.

* Mon Jan 19 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-14.fc11
- Resolves: rhbz#477373
- Used _fontdir macro instead of self-definition.
- Created common subpackage for common files.
- Created compat subpackage for uming backward compatibility.
- Refined descriptions.

* Wed Jan 14 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-13.fc11
- Resolves: rhbz#477373
- Included _font_pkg macro to conform new font packaging guidelines.
- Tidy up .spec file.

* Tue Jan 06 2009 Caius Chance <cchance at redhat.com> - 0.2.20080216.1-12.fc11
- Resolves: rhbz#477373 (Converted to new font packaging guidelines.)

* Sun Dec  7 2008 Behdad Esfahbod <besfahbo@redhat.com> - 0.2.20080216.1-10.fc11
- Don't umask before fc-cache.
- Add -f to fc-cache.

* Wed Oct 29 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-9.2.fc11
- Resolves: rhbz#466667 (Reverted to 0.2.20080216.1-4 without conf.avail.)

* Tue Oct 07 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-6.fc10
- Resolves: rhbz#465900 (Symlinks of fontconfig .conf files are inaccurated.)
- Macro'ed all __ln_s.

* Wed Oct 01 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-5.fc10
- Resolves: rhbz#459680 (Unsymlinked 25-ttf-arphic-uming-bitmaps.conf.)

* Tue Sep 30 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-4.fc10
- Resolves: rhbz#459680 (All .conf files are in fonts.avail and soft linked to
  fonts.d.)

* Mon Sep 30 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-3.fc10
- Resolves: rhbz#459680 (repatched)

* Mon Sep 29 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-2.fc10
- Resolves: rhbz#459680 (qt/kde: font antialiasing was disabled by uming 
  fontconfig file.)

* Tue Aug 05 2008 Caius Chance <cchance@redhat.com> - 0.2.20080216.1-1.fc10
- Resolves: rhbz#457868 (Update latest release fro upstream.)

* Mon Jun 30 2008 Caius Chance <cchance@redhat.com> - 0.1.20060928-6.fc10
- Refined obsoletes of fonts-chinese to be more ver-rel specific.

* Mon Jun 30 2008 Caius Chance <cchance@redhat.com> - 0.1.20060928-5.fc10
- Resolved: rhbz#453078 (fonts-chinese is deprecated and should be removed.)

* Fri Aug 31 2007 Jens Petersen <petersen@redhat.com>
- remove superfluous ttfmkdir requires

* Fri Aug 30 2007 Caius Chance <cchance@redhat.com> - 0.1.20060928-4.fc8
- Resolved: rhbz#253813 (New package separated from fonts-chinese)
-- Added requires and buildrequires ttfmkdir.

* Wed Aug 30 2007 Caius Chance <cchance@redhat.com> - 0.1.20060928-3.fc8
- Resolved: rhbz#253813 (New package separated from fonts-chinese)
-- Fixed cidmap directory and package requirements.

* Wed Aug 29 2007 Caius Chance <cchance@redhat.com> - 0.1.20060928-2.fc8
- Resolved: rhbz#253813 (New package separated from fonts-chinese)
-- Moved uming and ukai into sub-packages.
-- Moved fc-cache from post section to install section.
-- Fixed ghostscript directory and backward compatibilities symlinks.
-- Refined .spec literal, license, versioning contents.

* Wed Aug 22 2007 Caius Chance <cchance@redhat.com> - 0.1.20060928-1.fc8
- Resolved: rhbz#253813 (New package separated from fonts-chinese)
-- Review preparation.
